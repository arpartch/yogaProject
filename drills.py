import { map } from "ramda";
from functools import reduce;

######Map Function#####
# Capitalize words
names = ["peter", "athena", "alice", "bob"];
names2 = list(map(str.upper, names))
print(names2)

#Max out at 350
def sizeFunc(n):
    return n<=350
sizes = [200, 400, 350, 75, 1200];
sizes2 = map(sizeFunc, sizes)
print(list(sizes2))

# percentage of 50?
def percFunc(n):
    return n*2
percentages = [34, 33, 1, 0, 99, 123];
percentages2 = map(percFunc, percentages)
print(list(percentages2))

#Max from array
heartrates = [[80, 99], [120, 75], [115, 115]];
map(max, heartrates)
print (list(map(max, heartrates)))

## Have several things that you want to change into something else? Reduce it
fullNames = [["stradinger", "peter"], ["partch", "athena"]]; // -> ["Peter Stradinger", "Athena Partch"]

result = reduce(lambda item1, item2: item1 +item2)
print(result)


scores = [34, 33, 1, 0, 99, 123]; #48.33
print (functools.reduce(lambda a,b : a+b,lis)) 

## with full names (from above) -> [{firstName: "peter", lastName: "stradinger"},{firstName: "athena", lastName: "partch"}, ]

# Want to test if one or more things are true? Write a predicate (or set of predicates)
R.map(startsWith("a"), names); # -> [false, true, true, bob]
R.map(isGreaterThan300, sizes); # -> [false, true, true, false, true]
R.map(isEven, percentages); # -> [true, false, false, false?, false, false] I'm not sure if 0 is even

# Do something only if a predicate passes? Use a when
const animals = [{ type: "dog" }, { type: "cat" }, { type: "snake" }, { type: "shark" }];
# -> [true, true, false, false]
const balance = [10, 0, -3, 4, 50]; # -> ["ok", "ok", "overdrawn", "ok", "ok"] if the balance dips below 0

#If a predicate passes, do something, if not something else? Use an ifThen
const heights = [[4, 10], [5, 10], [5, 3], [6, 2]]; # ["reject", "ride", "reject", "ride"] height limit 5'5
const configs = [{ type: "text" }, { type: "date" }, { type: "datetime" }, { type: "text" }]; #-> ["Text", "Default", "Default", "Text"] use default unless text

#Have branching cases where you're looking for the first predicate that passes? Do a cond
const betterConfigs = [
  { type: "text" },
  { type: "date" },
  { type: "datetime" },
  { type: "text" },
  { type: "textarea" },
]; // -> ["Text", "Date", "Date", "Text", "TextArea"] use default unless text

#Want only part of a list that passes a predicate? use Filter (or reject)
const evenBetterConfigs = [
  { name: "Field A", type: "text", isEnabled: true },
  { name: "Field B", type: "date", isEnabled: false },
  { name: "Field C", type: "datetime", isEnabled: false },
  { name: "Field D", type: "text", isEnabled: true },
  { name: "Field E", type: "textarea", isEnabled: true },
];
# all enabled
# all disabled
# all enabled text fields
# all where the type starts with date

#Need to do a bunch of behaviors where you pass the result of one into another? Make a pipe
# for even better configs
# convertTypeToComponent, filterEnabled, sortByName, removeType
# Need to see what's happening at a step in the pipe? Use tap
# R.pipe(step1, R.tap(console.log), step2)(context) -> Tap will allow you to log out the result without interrupting the pipe
# Too much complexity? Refactor to a function (or several)

const context = {
  cards: [
    { id: 1, pose: "downward facing dog" },
    { id: 2, pose: "upward facing dog" },
    { id: 3, pose: "shivasana" },
    { id: 4, pose: "cat" },
    { id: 5, pose: "cow" },
    { id: 6, pose: "new pose" },
  ],
  default: "default",
};

# this is an ugly spaghetti function.
function formatCards(context) {
  const configs = R.prop("configs", context);
  const cards = R.map(config => {
    const id = R.prop("id", config);
    const card = { id };
    const pose = R.prop("pose", config);
    # format Label -> This should be refactored
    const labelWords = R.split(" ", pose);
    const capitalizedWords = R.map(word => {
      const firstLetter = R.head(word);
      const rest = R.tail(word);
      const capFirstLetter = R.toUpper(firstLetter);
      const capitalizedWord = R.concat(capFirstLetter, rest);
      return capitalizedWord;
    }, labelWords);
    const label = R.join(" ", capitalizedWords);
    # format image src -> this should also be refactored
    const srcWords = R.split(" ", pose);
    const capitalizedSrcTailWords = R.map(word => {
      const firstLetter = R.head(word);
      const rest = R.tail(word);
      const capFirstLetter = R.toUpper(firstLetter);
      const capitalizedWord = R.concat(capFirstLetter, rest);
      return capitalizedWord;
    }, R.tail(labelWords));
    const srcHead = R.head(srcWords);
    const srcWordsFormatted = R.prepend(srcHead, capitalizedSrcTailWords);
    const srcName = R.join("", srcWordsFormatted);
    const src = R.concat(srcName, ".jpg");
    const cardWithLabel = R.assoc("label", label, card);
    const cardWithSrc = R.assoc("src", src, cardWithLabel);
    const fullCard = cardWithSrc;
    return fullCard;
  }, configs);
  return cards;
}
const cards = [
  { id: 1, label: "Downward Facing Dog", src: "downwardFacingDog.jpg" },
  { id: 2, label: "Upward Facing Dog", src: "upwardFacingDog.jpg" },
  { id: 3, label: "Shivasana", src: "shivasana.jpg" },
  { id: 4, label: "Cat", src: "cat.jpg" },
  { id: 5, label: "Cow", src: "cow.jpg" },
  { id: 6, label: "New Pose", src: "default.jpg" },
];
# this is the first step of refactoring. Separating things out into functions
# see how this same function is used twice?
function capitalizeWords(words) {
  const firstLetter = R.head(word);
  const rest = R.tail(word);
  const capFirstLetter = R.toUpper(firstLetter);
  const capitalizedWord = R.concat(capFirstLetter, rest);
  return capitalizedWord;
}
# now see if you can also refactor format label and format image src into their own functions
function formatCards(context) {
  const configs = R.prop("configs", context);
  const cards = R.map(config => {
    const id = R.prop("id", config);
    const card = { id };
    const pose = R.prop("pose", config);
    // format Label -> This should be refactored
    const labelWords = R.split(" ", pose);
    const capitalizedWords = R.map(capitalizeWords, labelWords);
    const label = R.join(" ", capitalizedWords);
    // format image src -> this should also be refactored
    const srcWords = R.split(" ", pose);
    const capitalizedSrcTailWords = R.map(capitalizeWords, R.tail(labelWords));
    const srcHead = R.head(srcWords);
    const srcWordsFormatted = R.prepend(srcHead, capitalizedSrcTailWords);
    const srcName = R.join("", srcWordsFormatted);
    const src = R.concat(srcName, ".jpg");
    const cardWithLabel = R.assoc("label", label, card);
    const cardWithSrc = R.assoc("src", src, cardWithLabel);
    const fullCard = cardWithSrc;
    return fullCard;
  }, configs);
  return cards;