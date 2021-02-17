import { render, screen } from '@testing-library/react';
import * as R from "ramda"
import App from './App';

const capitalizeAll = (words) => words.map(word => R.toUpper(word))

test('capitalizeAll returns a capitalized list of strings', () => {
  const expectedResult = ["FOO", "BAR"]
  const words = ["foo", "bar"]
  const result = capitalizeAll(words)
  expect (result).toEqual(expectedResult)
});


test('capitalizeAll returns a different capitalized list of strings', () => {
  const expectedResult = ["BAR", "FOO"]
  const words = ["bar", "foo"]
  const result = capitalizeAll(words)
  expect (result).toEqual(expectedResult)
});