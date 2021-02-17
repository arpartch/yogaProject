import { render, screen } from '@testing-library/react';
import App from './App';

const capitalizeAll = () => ["FOO", "BAR"]

test('capitalizeAll returns a capitalized list of strings', () => {
  const expectedResult = ["FOO", "BAR"]
  const result = capitalizeAll()
  expect (result).toEqual(expectedResult)
});
