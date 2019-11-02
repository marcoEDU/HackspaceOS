function search(query) {
    axios.get("/search?q=" + query)
        .then(function (response) {
            if (query && query != '') {
                document.getElementById('search_bar').className = 'search_bar active'
                document.getElementById('search_results').innerHTML = response.data.html
            } else {
                document.getElementById('search_bar').className = 'search_bar'
                document.getElementById('search_results').innerHTML = ''
            }
        })
        .catch(function (error) {
            console.log(error);
        })
        .finally(function () {
            // always executed
        });
}