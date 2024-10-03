Title: JS Lab
date: 2024-07-17
tags: curl, http, socket, socketserver <!-- @LT-IGNORE:MORFOLOGIK_RULE_EN_CA(http)@ -->
authors: Hazel Victoria Campbell
status: Published
summary: Lab Procedure, Lab Assignments, Lab Marking
----

<style>
    html body main {
        background-image: url("/theme/draft.png");
        background-repeat: repeat;
        background-size: 100%;
    }
</style>

# Description

In this lab you will make a JS Clock/Timer/Alarm/Stopwatch "single-page" app.
The app won't require any network traffic except loading a single HTML file.
You will use DHTML, promises, and async/await to connect your code and make sure each piece of code runs at the same time, and that the Clock, Timer, Alarm, and Stopwatch functions all work at the same time, independently.

## Learning Goals

* Basic DOM manipulation
* A thorough understanding of promises, async, await.
* Combining JS, HTML, and CSS into a single file.

# Getting Started

1. Get the GitHub classroom link from eClass, create your assignment, and clone it.
2. Create an appropriate `.gitignore` file, to prevent unwanted files being committed to your repository. (See Django/Heroku labs for tips.)

<!-- 
# Install Webpack

Webpack is a bundler/transpiler like esbuild.

```sh
npm install --save-dev webpack webpack-cli @webpack-cli/generators webpack-html-plugin mini-css-extract-plugin
```

## Start a Webpack project

```sh
npx webpack init
```

Webpack will ask you a bunch of questions. Since we're using plain JS, HTML and CSS, we can answer it like this:

```txt
? Which of the following JS solutions do you want to use? ES6
? Do you want to use webpack-dev-server? No
? Do you want to simplify the creation of HTML files for your bundle? Yes
? Do you want to add PWA support? No
? Which of the following CSS solutions do you want to use? CSS only
? Will you be using PostCSS in your project? No
? Do you want to extract CSS for every file? No
? Do you like to install prettier to format generated configuration? Yes
? Pick a package manager: npm
[webpack-cli] ℹ INFO  Initialising project...
 conflict package.json
? Overwrite package.json? overwrite
```

Webpack will create a README, index.html, src/index.js for you. You will have to create your own CSS file.


## Configure Webpack

Add some options the style loader (it loads the CSS):

```js
const stylesHandler = {
    loader: 'style-loader',
    options: {
        insert: 'head',
        injectType: 'singletonStyleTag'
    }
};
```

Set the output file explicitly in `webpack.config.js`:

```js
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'main.js',
    },
```

Set `inject` to `false` for the options of `HtmlWebpackPlugin` in `webpack.config.js`,
and make sure to load the `MiniCssExtractPlugin`:

```js
    plugins: [
        new HtmlWebpackPlugin({
            template: 'index.html',
            filename: 'output.html',
            inject: false,
        }),
        new MiniCssExtractPlugin(),
    ],
```

Setting `inject` to `false` prevents the `HtmlWebpackPlugin` from trying to load the transpiled JS output of webpack as a separate file. Instead, we'll insert it directly into our `<head>`:

```html
    <script defer="defer">
        <%= compilation.assets[webpackConfig.output.filename].source() %>
    </script>
    <style type="text/css">
        <%= compilation.assets['main.css'].source() %>
    </style>
```

We also need to have MiniCssExtractPlugin load our styles:

```js
            {
                test: /\.css$/i,
                use: [MiniCssExtractPlugin.loader,'css-loader'],
            },
```

## Use Webpack

We can run webpack with one of the commands defined in the `package.json` that webpack built for us,
such as `npm run build`. When this runs you should get an output `index.html` file in the `dist` directory. Make sure to add the `dist` directory to your `.gitignore`!

Check the `index.html` that webpack built in your `dist` directory to make sure it includes the JavaScript from your `index.js` file. If you haven't changed your input `index.js` (the one in the `src` directory), it should contain a `console.log` right in the output `index.html`.
-->

# Requirements

* All JS and CSS are included in the single HTML file.

# Submission Instructions

Make sure you push to GitHub classroom **BEFORE 4PM on the day of your lab section!** You will not be able to push after that!

Submit a link to your repo in the form `https://github.com/uofa-cmput404/w24-h0x-labsignment-js-yourgithubname`. **Do not** submit a link to a branch, a file, or the clone URL. If you do not do this we will not know which GitHub submission is yours.

<p class="warning">If you do not submit a link to your repo on eClass on time using the correct format above, you will get a zero.</p>
]