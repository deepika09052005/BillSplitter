
const form = document.getElementById("billForm");
const result = document.getElementById("result");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const amount = Number(
        document.getElementById("billAmount").value
    );
    const people = Number(
        document.getElementById("people").value
    );
    const description =
        document.getElementById("description").value.trim();

    if (!Number.isFinite(amount) || amount <= 0 ||
        !Number.isSafeInteger(people) || people < 1) {
        result.className = "error";
        result.textContent = "Enter valid bill details.";
        return;
    }

    result.className = "";
    result.textContent = "Saving bill...";

    try {
        const response = await fetch("/api/bills", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                amount: amount,
                people: people,
                description: description
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Could not save bill.");
        }

        result.className = "success";
        result.replaceChildren();

        const heading = document.createElement("h3");
        heading.textContent = "Bill Saved Successfully!";
        result.appendChild(heading);

        const details = document.createElement("p");
        details.textContent =
            `Description: ${data.description}`;
        result.appendChild(details);

        const total = document.createElement("p");
        total.textContent =
            `Total bill: ₹${Number(data.amount).toFixed(2)}`;
        result.appendChild(total);

        const count = document.createElement("p");
        count.textContent = `People: ${data.people}`;
        result.appendChild(count);

        const share = document.createElement("p");
        share.textContent =
            `Each person pays approximately ₹${Number(data.share).toFixed(2)}.`;
        result.appendChild(share);

        const saved = document.createElement("p");
        saved.textContent = `Saved bill ID: ${data.id}`;
        result.appendChild(saved);

    } catch (error) {
        result.className = "error";
        result.textContent = error.message;
    }
});
