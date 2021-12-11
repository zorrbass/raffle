# raffle

The fetch of the delegator list and the input of the epoch nonce need to be done independently.

* Get the list of delegators at the epoch change.
* Get the epoch nonce aprox. 1.5 days prior to the next epoch change.
* It is recommended to run the code in jupyter in order to save the delegator list first. 

* IMPORTANT - the index in the participants list starts with 0 since the mod operation with the epoch nonce and the number of participants will result in a number from 1 to (participants - 1)



## **Epoch Nonce 307:** 
`c9df45e52ba90cd0fd84a2150ab3764e36de44193f98fafda38c79f90e825a7b`

## **Epoch Nonce 308:** 
`2b842312f5ca76bc0abe210d5d575336b7fa7bd2fa8a2838cb0ee3ef0b3c9c0b`
