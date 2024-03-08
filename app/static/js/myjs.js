

document.getElementById('categorieSelect').addEventListener('change', function() {
    var selectedCategorieId = this.value;
    var rows = document.querySelectorAll('tbody tr');

    rows.forEach(function(row) {
        var rowCategorieIds = row.getAttribute('data-categorie-ids').split(','); // Récupérer les IDs des catégories du livre
        
        if (selectedCategorieId === "" || rowCategorieIds.includes(selectedCategorieId)) {
            row.style.display = ''; // Afficher la ligne si la catégorie correspond ou si aucune catégorie n'est sélectionnée
        } else {
            row.style.display = 'none'; // Cacher la ligne si la catégorie ne correspond pas
        }
    });
});


document.getElementById('ChercheInput').addEventListener('keyup', function() {
    var searchValue = this.value.toLowerCase();
    var tableRows = document.getElementById('Listlivreid').getElementsByTagName('tbody')[0].getElementsByTagName('tr');
    
    for (var i = 0; i < tableRows.length; i++) {
        var currentRowTitle = tableRows[i].getElementsByTagName('td')[0]; // 0 pour la première colonne (titre)
        var currentRowAuthors = tableRows[i].getElementsByTagName('td')[6]; // 6 pour la 7éme colonne (auteurs)
        
        if (currentRowTitle && currentRowAuthors) {
            var textValueTitle = currentRowTitle.textContent || currentRowTitle.innerText;
            var textValueAuthors = currentRowAuthors.textContent || currentRowAuthors.innerText;
            
            if (textValueTitle.toLowerCase().indexOf(searchValue) > -1 || textValueAuthors.toLowerCase().indexOf(searchValue) > -1) {
                tableRows[i].style.display = "";
            } else {
                tableRows[i].style.display = "none";
            }
        }          
    }
});

document.addEventListener('DOMContentLoaded', function() {
    // Écoutez les changements sur le select d'auteurs
    document.getElementById('auteurSelect').addEventListener('change', function() {
      var selectedAuteurId = this.value;
      var rows = document.querySelectorAll('#Listlivreid tbody tr');
  
      rows.forEach(function(row) {
        // Supposons que chaque ligne de livre a un attribut data-auteurs-ids qui contient les IDs des auteurs séparés par des virgules
        var rowAuteursIds = row.getAttribute('data-auteurs-ids').split(',');
  
        if (selectedAuteurId === "" || rowAuteursIds.includes(selectedAuteurId)) {
          row.style.display = ''; // Affiche la ligne
        } else {
          row.style.display = 'none'; // Cache la ligne
        }
      });
    });
  });