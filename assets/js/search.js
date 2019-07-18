(function() {

    function displaySearchResults(results, store, searchTerm) {
      var searchResults = document.getElementById('search-results');
  
      if (results.length) {
        var appendString = '';
  
        for (var i = 0; i < results.length; i++) {  // Iterate over the results
          var item = store[results[i].ref];
          var content = formatContentString(item.content, searchTerm);
          appendString += "<li>";
          appendString +=   "<a class='result' href='" + item.url + "?q=" + searchTerm + "'><h3>" + item.title + "</h3></a>";
          appendString +=   "<div class='snippet'>" + content + "</div>";
          appendString += "</li>"
        }
  
        return appendString;
      } else {
        return '<li>No results found</li>';
      }
    }
  
    function getQueryVariable(variable) {
      var query = window.location.search.substring(1);
      var vars = query.split('&');
  
      for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
  
        if (pair[0] === variable) {
          return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
        }
      }
    }

    function formatContentString(str, searchTerm){
      var termIdx = str.toLowerCase().indexOf(searchTerm.toLowerCase());
        if (termIdx >= 0) {
            var startIdx = Math.max(0, termIdx - 140);
            var endIdx = Math.min(str.length, termIdx + searchTerm.length + 140);
            var trimmedContent = (startIdx === 0) ? "" : "&hellip;";
            trimmedContent += str.substring(startIdx, endIdx);
            trimmedContent += (endIdx >= str.length) ? "" : "&hellip;"

            var highlightedContent = trimmedContent.replace(new RegExp(searchTerm, "ig"), function matcher(match) {
                return "<strong>" + match + "</strong>";
            });

            return highlightedContent;
        }
        else {
            var emptyTrimmedString = str.substr(0, 280);
            emptyTrimmedString += (str.length < 280) ? "" : "&hellip;";
            return emptyTrimmedString;
        }
    }
  
    var searchTerm = getQueryVariable('query');
  
    if (searchTerm) {
      //document.getElementById('search-box').setAttribute("value", searchTerm);

      // Initalize lunr with the fields it will be searching on. I've given title
      // a boost of 10 to indicate matches on this field are more important.
      var idx = lunr(function () {
        this.field('id');
        this.field('title', { boost: 10 });
        this.field('content');
      });
      for (var key in window.store) { // Add the data to lunr)
        idx.add({
          'id': key,
          'title': window.pages[key].title,
          'content': window.pages[key].content
        });
  
        var results = idx.search(searchTerm); // Get lunr to perform a search
        document.querySelector("#search-results").innerHTML = displaySearchResults(results, window.store, searchTerm);
      }
    }
  })();
  