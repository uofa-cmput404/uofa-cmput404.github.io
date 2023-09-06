'use strict';

var assert = chai.assert;
const tabWidth = 2;


function extract_text(e) {
  let text = "";
  for (let child of e.childNodes) {
    if (child.nodeName === "SPAN") {
      text += extract_text(child);
    } else if (child.nodeName === "#text") {
      text += child.wholeText;
    } else if (child.nodeName === "BR") {
      text += "\n";
    } else {
      // ??? unexpected kind of node in the code
      console.log("Unexpected contents: ");
      console.log(child);
    }
  }
  return text;
}

function fiddler() {
  let codes = document.querySelectorAll('section pre>code');
  for (let code of codes) {
    let pre = code.parentElement;
    assert(pre.nodeName === 'PRE');
//     console.log(String(code.classList));
    let existing = pre.querySelector('.fiddler');
    if (existing) {
//       console.log("already made a button here ");
    } else {
      let newForm = document.createElement("form");
//       console.log("need a button here");
      let newButton = document.createElement("button");
      newForm.className = "fiddler";
      newForm.method = "POST";
      newForm.action = "https://jsfiddle.net/api/post/library/pure";
      if (code.classList.contains('javascript')) {
        newButton.name = "js";
      } else if (
        code.classList.contains('html') 
        || code.classList.contains('xml') 
      ) {
        newButton.name = "html";
      } else if (code.classList.contains('css')) {
        newButton.name = "css";
      } else {
//         console.log(String("What's this: " + code.classList));
        continue;
      }
      let text = extract_text(code);
      newButton.value = text;
      newButton.type = "submit";
      newButton.appendChild(
        document.createTextNode("Fiddle!")
        );
      newForm.appendChild(newButton);
      pre.insertBefore(newForm, null);
      setTimeout( () => {
        newButton.style.marginBottom = (newButton.clientHeight * -1) + 'px';
      }, 0);
    }
  }
}

function stripPreIndentation() {
  let codes = document.querySelectorAll('pre>code');
  for (let code of codes) {
    let pre = code.parentElement;
    assert(pre.nodeName === 'PRE');
    let script = code.querySelector('script');
    if (script) {
      var guts = script.innerHTML;
    } else {
      var guts = code.innerHTML;
    }
    if (guts.includes('<')) {
      guts = guts.replace(/</g, "&lt;");
    }
    let lines = guts.split(/\r\n|\r|\n/); // https://stackoverflow.com/a/5035058 2019-02-13
//     console.log(lines);
    if (lines[0].match(/^[\s]*$/)) {
      lines.shift();
    }
    if (lines[lines.length-1].match(/^[\s]*$/)) {
      lines.pop();
    }
    let minIndent = Infinity;
    for (let line of lines) {
      line = line.replace(/\t/g, ' '.repeat(tabWidth));
//       console.log(line);
      let indented = (line.match(/^ *[^ ]+/));
      if (indented) {
        indented = indented[0];
        let indent = (indented.match(/^ */))[0].length;
        if (indent < minIndent) {
          minIndent = indent;
        }
      }
    }
    if (minIndent === Infinity) {
      minIndent = 0;
    }
    let indentRegex = RegExp('^' + ' '.repeat(minIndent));
    let newLines = [];
    for (let line of lines) {
      let newLine = line.replace(indentRegex, '');
      newLines.push(newLine);
    }
    let newGuts = newLines.join("\n");
    code.innerHTML = newGuts;
    hljs.highlightBlock(code);
  }
}

function blackStyleSheet() {
  document.getElementById("revealtheme").setAttribute("href", "node_modules/reveal.js/css/theme/black.css");
  document.getElementById("highlighttheme").setAttribute("href", "node_modules/highlightjs/styles/dracula.css");
  document.getElementById("404theme").setAttribute("href", "cmput404-slides-black.css");
}

function whiteStyleSheet() {
  document.getElementById("revealtheme").setAttribute("href", "node_modules/reveal.js/css/theme/white.css");
  document.getElementById("highlighttheme").setAttribute("href", "node_modules/highlightjs/styles/googlecode.css");
  document.getElementById("404theme").setAttribute("href", "cmput404-slides-white.css");
}

function fixTitle() {
  var firsth2 = document.querySelector("section h2");
  var title = document.querySelector("title");
  title.innerText = title.innerText + " - " + firsth2.innerText;
}

//-- Initialize Slide Deck -----------------------------------------------------
/* From reveal.js */
var link = document.createElement( 'link' );
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = window.location.search.match( /print-pdf/gi ) ? 'node_modules/reveal.js/css/print/pdf.css' : 'node_modules/reveal.js/css/print/paper.css';
document.getElementsByTagName( 'head' )[0].appendChild( link );
/* end from reveal.js */

window.addEventListener("DOMContentLoaded", (event) => {
  // dom exists
  fixTitle();

  whiteStyleSheet(); // this is the default
});

window.addEventListener("load", (event) => {
  // scripts have loaded
  
  stripPreIndentation();
  // Initialize Reveal
  Reveal.initialize({
    dependencies: [{
        src: 'node_modules/reveal.js/plugin/markdown/marked.js'
      },
      {
        src: 'node_modules/reveal.js/plugin/markdown/markdown.js'
      },
      {
        src: 'node_modules/reveal.js/plugin/notes/notes.js',
        async: true
      },
      {
        src: 'node_modules/reveal.js-menu/menu.js'
      }
    ],
    // The "normal" size of the presentation, aspect ratio will be preserved
    // when the presentation is scaled to fit different resolutions. Can be
    // specified using percentage units.
    //         width: 960,
    //         height: 700,
    width: 960,
    height: 720,

    // Factor of the display size that should remain empty around the content
    margin: 0.0,

    // Bounds for smallest/largest possible scale to apply to content
    minScale: 0.01,
    maxScale: 5,
    menu: {
      hideMissingTitles: true,
      titleSelector: 'h1, h2, h3',
    },
    history: true,
  });

  // Fiddle with things
  Reveal.addEventListener('ready', function(event) {
    // event.previousSlide, event.currentSlide, event.indexh, event.indexv
    fitty.fitAll();
    fiddler();
    Reveal.layout(); // just in case
  });

  // add emojis
  twemoji.parse(document.body);

  // initilize fitty
  fitty('.fit');
});
