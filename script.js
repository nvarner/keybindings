const program = document.querySelector("#program");
const keybinding = document.querySelector("#keybinding");
const form = document.querySelector("#form");
const results = document.querySelector("#results");
const message = document.querySelector("#message");

form.addEventListener("submit", (e) => {
    while (results.hasChildNodes()) {
        results.removeChild(results.firstChild);
    }
    while (message.hasChildNodes()) {
        message.removeChild(message.firstChild);
    }

    ajax("http://nathanvarner.com/keybindings/manifest.list", (response) => {
        programName = program.value.toLowerCase();
        programSupported = response.responseText.split("\n").includes(programName);

        if (programSupported) {
            ajax("http://nathanvarner.com/keybindings/" + programName + ".json", (response) => {
                responseObject = JSON.parse(response.responseText);
                keybindingsObject = responseObject["keybindings"];
                regex = toRegex(keybinding.value);

                foundAny = false;
                for (const description in keybindingsObject) {
                    if (description.search(regex) !== -1) {
                        foundAny = true;
                        keybindings = keybindingsObject[description];
                        if (typeof(keybindings) === "string") {
                            keybindings = [keybindings];
                        }
                        keybindings.forEach((keybinding) => {
                            const item = document.createElement("li");
                            const text = document.createTextNode(htmlspecialchars(description) + ": " +
                                htmlspecialchars(keybinding));
                            item.appendChild(text);
                            results.appendChild(item);
                        });
                    }
                }

                if (!foundAny) {
                    const text = document.createTextNode("There are no such keybindings for " +
                        htmlspecialchars(program.value));
                    message.appendChild(text);
                }
            });
        } else {
            const text = document.createTextNode(htmlspecialchars(program.value)
                + " isn't one of the supported programs");
            message.appendChild(text);
        }
    });

    e.preventDefault();
});

function ajax(url, success, fail) {
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.addEventListener("readystatechange", () => {
        if (xmlhttp.readyState == XMLHttpRequest.DONE) {
           if (xmlhttp.status == 200) {
               success(xmlhttp);
           }
           else {
               fail();
           }
        }
    });

    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

function toRegex(search) {
    searchArray = search.split(" ");
    pattern = "(" + searchArray.join("|") + ")+";
    return new RegExp(pattern, "i");
}

function htmlspecialchars(badText) {
    badText.replace("&", "&amp;");
    badText.replace("\"", "&quot;");
    badText.replace("'", "&apos;");
    badText.replace("<", "&lt;");
    badText.replace(">", "&gt;");
    return badText;
}
