function redirectToPage(url) {
    window.location.href = url; 
}


const facts = [
    "Employees are entitled to 5.6 weeks of paid holiday per year.",
    "Employees who have worked for their employer for at least 26 weeks have the legal right to request flexible working arrangements.",
    "Unfair dismissal claims can be made by employees who have been employed for at least two years.",
    "The standard inheritance tax rate is 40%, charged on the portion of an estate valued over £325,000.",
    "Law mandates that all eligible workers must be automatically enrolled in a workplace pension by their employer.",
    "Divorce requires proving the marriage has irretrievably broken down based on one of five facts: adultery, unreasonable behaviour, desertion, two years' separation with consent, or five years' separation without consent.",
    "Inheritance can be contested under the Inheritance (Provision for Family and Dependants) Act 1975 if dependants believe they have not received reasonable financial provision."
];


function displayFact() {
    const randomIndex = Math.floor(Math.random() * facts.length);
    document.getElementById('fact-text').innerText = facts[randomIndex];
}