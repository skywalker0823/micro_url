document.addEventListener("DOMContentLoaded", () => {
    console.log("loha")
});

action = async() => {
    let address = document.getElementById("address").value
    console.log(address)
    const options = {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
        address: address,
        }),
    };
    const response = await fetch("/micro", options);
    const result = await response.json();
    if (result.ok) {
        console.log("註冊成功!");
    } else {
        console.log("error!");
    }
}
