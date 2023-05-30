const URL = "http://localhost:8080";

// Solve page (Sudoku component) requests
const prompt = async (input) =>{
    return await fetch(URL+"/prompt", {
        // Adding method type
        method: "POST",
        // Adding body or contents to send
        body: JSON.stringify({
            input:input
        }),
        // Adding headers to the request
        headers: {
            "Content-type": "application/json; charset=UTF-8"
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
