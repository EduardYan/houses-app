// Some utils functions to use

// message for use for ask
const messageForAsk = 'You want delete this house?';

/**
 * 
 * @returns The result of the a confirm message.
 */
export const askIfDelete = () => {
  const result = confirm(messageForAsk);
  return result;
}