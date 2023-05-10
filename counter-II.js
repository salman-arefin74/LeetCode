var createCounter = function(init) {
    let initialValue = init;
    return {
        increment(){
            return ++init;
        },
        decrement(){
            return --init;
        },
        reset(){
            init = initialValue;
            return init;
        }
    }
};
