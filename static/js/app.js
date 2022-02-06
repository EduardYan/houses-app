// Javascript for the app

import { askIfDelete } from "./utils.js";

// for ask if delete the house
const buttonsList = document.querySelectorAll('.delete-button');
buttonsList.forEach((button) => {
  button.addEventListener('click', (e) => {
    const result = askIfDelete();
    if (!result) {
      // eviting not refresh
      e.preventDefault();
    }
  });
});