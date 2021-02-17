import { map } from "ramda";
from functools import reduce;

######Map Function#####
# Capitalize words
def capitalize(name):
    return name.capitalize()


x = map(capitalize, names)
print(list(x))

#Max out at 350
def max_out_350(size):
    return size if size <= 350 else 350

sizes = [200, 400, 350, 75, 1200]
x = map(max_out_350, sizes)
print(list(x))

# percentage of 50?
def percentage(num):
    return num/50

percentages = [34, 33, 1, 0, 99, 123]
x = map(percentage, percentages)
print(list(x))


#Max from each pair
def max_num(pair):
    return max(pair)

heartrates = [[80, 99], [120, 75], [115, 115]]
x = map(max_num, heartrates)
print(list(x))


## Have several things that you want to change into something else? Reduce it
fullNames = [["stradinger", "peter"], ["partch", "athena"]]; // -> ["Peter Stradinger", "Athena Partch"]


scores = [34, 33, 1, 0, 99, 123]; #48.33
print (functools.reduce(lambda a,b : a+b,lis)) 

## with full names (from above) -> [{firstName: "peter", lastName: "stradinger"},{firstName: "athena", lastName: "partch"}, ]

# Want to test if one or more things are true? Write a predicate (or set of predicates)
R.map(startsWith("a"), names); # -> [false, true, true, bob]
R.map(isGreaterThan300, sizes); # -> [false, true, true, false, true]
R.map(isEven, percentages); # -> [true, false, false, false?, false, false] I'm not sure if 0 is even

x = map(lambda a: a.startswith('a'), names)
print(list(x))

x = map(lambda a: a > 300, sizes)
print(list(x))

x = map(lambda a: a % 2 == 0, percentages)
print(list(x))


# Do something only if a predicate passes? Use a when
# -> [true, true, false, false]

animals = [{ type: "dog" }, { type: "cat" }, { type: "snake" }, { type: "shark" }]

x = map(lambda ani: ani[type] == 'dog' or ani[type] == 'cat', animals)
print(list(x))

# ->if the balance dips below 0
 balance = [10, 0, -3, 4, 50] #["ok", "ok", "overdrawn", "ok", "ok"] 
x = map(lambda y: 'ok' if y>0 else 'overdrawn', balance)
print(list(x))

#If a predicate passes, do something, if not something else? Use an ifThen

heights = [[4, 10], [5, 10], [5, 3], [6, 2]] # ["reject", "ride", "reject", "ride"] height limit 5'5
x = map(lambda y: 'ride' if y[0]*12 + y[1] >= 5.5*12 else 'reject', heights)
print(list(x))

configs = [{ type: "text" }, { type: "date" }, { type: "datetime" }, { type: "text" }]; #-> ["Text", "Default", "Default", "Text"] use default unless text
x = x = map(lambda conf: 'Text' if conf[type] == 'text' else 'Default', configs)
print(list(x))

#Have branching cases where you're looking for the first predicate that passes? Do a cond
betterConfigs = [
  { type: "text" },
  { type: "date" },
  { type: "datetime" },
  { type: "text" },
  { type: "textarea" },
]; # -> ["Text", "Date", "Date", "Text", "TextArea"] use default unless text

def predicate(x):
    if x[type] == 'text':
        return 'Text'
    elif x[type] == 'date' or x[type] == 'datetime':
        return 'Date'
    elif x[type] == 'textarea':
        return 'TextArea'


x = map(predicate, betterConfigs)
print(list(x))


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

context = {
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
   configs = R.prop("configs", context);
   cards = R.map(config => {
     id = R.prop("id", config);
     card = { id };
     pose = R.prop("pose", config);
    # format Label -> This should be refactored
     labelWords = R.split(" ", pose);
     capitalizedWords = R.map(word => {
       firstLetter = R.head(word);
       rest = R.tail(word);
       capFirstLetter = R.toUpper(firstLetter);
       capitalizedWord = R.concat(capFirstLetter, rest);
      return capitalizedWord;
    }, labelWords);
     label = R.join(" ", capitalizedWords);
    # format image src -> this should also be refactored
     srcWords = R.split(" ", pose);
     capitalizedSrcTailWords = R.map(word => {
       firstLetter = R.head(word);
       rest = R.tail(word);
       capFirstLetter = R.toUpper(firstLetter);
       capitalizedWord = R.concat(capFirstLetter, rest);
      return capitalizedWord;
    }, R.tail(labelWords));
     srcHead = R.head(srcWords);
     srcWordsFormatted = R.prepend(srcHead, capitalizedSrcTailWords);
     srcName = R.join("", srcWordsFormatted);
     src = R.concat(srcName, ".jpg");
     cardWithLabel = R.assoc("label", label, card);
     cardWithSrc = R.assoc("src", src, cardWithLabel);
     fullCard = cardWithSrc;
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
   firstLetter = R.head(word);
   rest = R.tail(word);
   capFirstLetter = R.toUpper(firstLetter);
   capitalizedWord = R.concat(capFirstLetter, rest);
  return capitalizedWord;
}
# now see if you can also refactor format label and format image src into their own functions
function formatCards(context) {
   configs = R.prop("configs", context);
   cards = R.map(config => {
     id = R.prop("id", config);
     card = { id };
     pose = R.prop("pose", config);

    
    # format Label -> This should be refactored
    labelWords = R.split(" ", pose);
    capitalizedWords = R.map(capitalizeWords, labelWords);
    label = R.join(" ", capitalizedWords);

def format_label(x):
    splitted = x.split(' ')
    splitted = map(lambda y: y.capitalize(), splitted)
    return ' '.join(list(splitted))



    # format image src -> this should also be refactored
    srcWords = R.split(" ", pose);
    capitalizedSrcTailWords = R.map(capitalizeWords, R.tail(labelWords));
    srcHead = R.head(srcWords);
    srcWordsFormatted = R.prepend(srcHead, capitalizedSrcTailWords);
    srcName = R.join("", srcWordsFormatted);
    src = R.concat(srcName, ".jpg");
    cardWithLabel = R.assoc("label", label, card);
    cardWithSrc = R.assoc("src", src, cardWithLabel);
    fullCard = cardWithSrc;
    return fullCard;
  }, configs);
  return cards;

  def format_img_src(x):
        splitted = x.split(' ')
    splitted = map(lambda y: y.capitalize(), splitted)
    return ' '.join(list(splitted))

    def formater(x):
        x['label'] = format_label(x['label'])
    x['src'] = format_img_src(x['src'])
    return x

x = map(formater, cards)
print(list(x))