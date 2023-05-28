// Solve page (Sudoku component) requests
const solve = async (sudoku, size) =>{
    return await fetch(URL+"/solve", {
        // Adding method type
        method: "POST",
        // Adding body or contents to send
        body: JSON.stringify({
            sudoku: sudoku,
            size: size
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

// Find page requests
const scrape = async (index, difficulty) =>{
    return await fetch(URL+"/scrape", {
    // Adding method type
    method: "POST",
    // Adding body or contents to send
    body: JSON.stringify({
        index: index,
        difficulty: difficulty
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