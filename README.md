# raffle

The fetch of the delegator list and the input of the epoch nonce need to be done independently.

* Get the list of delegators at the epoch change.
* Get the epoch nonce aprox. 1.5 days prior to the next epoch change.
* It is recommended to run the code in jupyter in order to save the delegator list first. 

* IMPORTANT - the index in the participants list starts with 0 since the mod operation with the epoch nonce and the number of participants will result in a number from 1 to (participants - 1)
