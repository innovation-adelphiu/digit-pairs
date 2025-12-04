Array.prototype.shuffle = function() 
{
    let currentIndex = this.length;
    let randomIndex = 0;

    // while elements remain to be shuffled
    while (currentIndex !== 0) 
    {
        // pick a random element
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        // swap with current element
        [this[currentIndex], this[randomIndex]] = [this[randomIndex], this[currentIndex]];
    }

    // return the shuffled array for method chaining
    return this; 
};

// this is necessary because .sort() uses string sorting
Array.prototype.numericSort  = function()
{
    // return the shuffled array for method chaining
    return this.sort((a, b) => a - b);
} 