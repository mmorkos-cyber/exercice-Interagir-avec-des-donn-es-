fetch("produits_complet.json")
  .then(res => res.json())
  .then(data => {
    afficherProduits(data["produits"]);
    console.log(data["produits"])
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