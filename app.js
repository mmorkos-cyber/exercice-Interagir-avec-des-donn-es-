fetch("produits_complet.json")
  .then(res => res.json())
  .then(data => {
    afficherProduits(data["produits"]);
    afficherRupture(data.produitRupture);
    afficherValeurCategorie(data.valeurMarchande);
    afficherValeurTotale(data.valeurTotale);
  });

  function afficherProduits(produits) {
  const liste = document.querySelector("#liste-produits");
  liste.innerHTML = "";
  produits.forEach(p => {
    const li = document.createElement("li");
    li.textContent = `${p.nom} — ${p.prix}€ — Stock: ${p.stock}`;
    liste.appendChild(li);
  });
}

function afficherRupture(produitRupture) {
  const rupt = document.querySelector("#rupture");
  rupt.innerHTML = "";
  produitRupture.forEach(pr => {
    const li = document.createElement("li");
    li.textContent = `${pr}`;
    rupt.appendChild(li);
  })
}

function afficherValeurCategorie(valeurMarchande) {
  const marchande = document.querySelector("#valeur-categorie");
  marchande.innerHTML = "";
  valeurMarchande.forEach(vm => {
    const li = document.createElement("li");
    li.textContent = `${vm.categorie} — ${vm.marchandes}`;
    marchande.appendChild(li);
  })
}

function afficherValeurTotale (valeurTotale) {
  const totale = document.querySelector("#valeur-totale");
  totale.innerHTML = valeurTotale[0][0];
}