const URL = "http://127.0.0.1:8080";

// Solve page (Sudoku component) requests
export const prompt = async (input) =>{
    if(input.length >= 1){
        return await fetch(URL+"/prompt", {
            // Adding method type
            method: "POST",
            // Adding body or contents to send
            body: JSON.stringify({
                input:input
            }),
            // Adding headers to the request
            headers: {
                "Content-type": "application/json; charset=UTF-8",
                'Access-Control-Allow-Origin':'http://localhost:3000'
            }
            })
            // Converting to JSON
            .then((response) => {
                return response.json()
            }).then((data) =>{
                console.log(data)
                return data.body
            })
    }
}
