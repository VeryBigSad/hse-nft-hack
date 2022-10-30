let el_up = document.getElementById("GFG_UP");

    //       "background": ["ocean", "deep sea", "beach"],
    //     "head": ["shark", "human", "fish"],
    //     "clothing": ["wet suit", "scuba gear", "swimming trunks"]
    //
           

let list = [
    {"background": ["ocean", "deep sea", "beach"]},
    {"head": ["shark", "human", "fish"]},
    {"clothing": ["wet suit", "scuba gear", "swimming trunks"]}
];

el_up.innerHTML = "Click on the button to create "
        +   "the table from the JSON data.<br><br>"
        + JSON.stringify(list[0]) + "<br>"
        + JSON.stringify(list[1]) + "<br>"
        + JSON.stringify(list[2]);  
    
generator.addEventListener('click', () => {
    
})


function constructTable(selector) {
    
    // Getting the all column names
    let cols = Headers(list, selector); 

    // Traversing the JSON data
    for (let i = 0; i < list.length; i++) {
        let row = $('<tr/>');  
        for (let colIndex = 0; colIndex < cols.length; colIndex++)
        {
            let val = list[i][cols[colIndex]];
            
            // If there is any key, which is matching
            // with the column name
            if (val == null) val = ""; 
                row.append($('<td/>').html(val));
        }
        
        // Adding each row to the table
        $(selector).append(row);
    }
}

function Headers(list, selector) {
    let columns = [];
    let header = $('<tr/>');
    
    for (let i = 0; i < list.length; i++) {
        let row = list[i];
        
        for (let k in row) {
            if ($.inArray(k, columns) == -1) {
                columns.push(k);
                
                // Creating the header
                header.append($('<th/>').html(k));
            }
        }
    }
    
    // Appending the header to the table
    $(selector).append(header);
        return columns;
}