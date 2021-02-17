import { render, screen } from '@testing-library/react';
import * as R from "ramda"
import App from './App';

// direct access - when you know for a fact the list will contain a certain number of elements (tuples, x&y coordinates)
const capitalizeAllDirect = (words) => {
  const first = words[0]
  const second = words[1]
  console.log(words)
  return [R.toUpper(first), R.toUpper(second)]
}


// for loop - when you know how long you want to loop to be but you want to be able to vary how long the loop is
const capitalizeAllFor = (words) => {
  const newWords = []
  for(let i = 0; i < words.length; i++){
    newWords.push(R.toUpper(words[i]))
  }
  return newWords
}


// map - normal way | iterate over an array of stuff calling the supplied function once for each thing, passing the thing in as the only property 
const capitalizeAllMap = words => words.map(word => R.toUpper(word))

// functional map - the functional way in which we pass the function and the array into map and call the function once for each thing with the thing as the only property 

const capitalizeAll = R.map(R.toUpper)

//tests

test.only('capitalizeAll returns a capitalized list of strings', () => {
  const expectedResult = ["FOO", "BAR", "FUN"]
  const words = ["foo", "bar", "fun"]
  const result = capitalizeAll(words)
  expect (result).toEqual(expectedResult)
});


test('capitalizeAll returns a different capitalized list of strings', () => {
  const expectedResult = ["BAR", "FOO"]
  const words = ["bar", "foo"]
  const result = capitalizeAll(words)
  expect (result).toEqual(expectedResult)
});