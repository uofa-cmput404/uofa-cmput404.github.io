Title: JS Lab
date: 2024-07-17
tags: javascript, webapp <!-- @LT-IGNORE:MORFOLOGIK_RULE_EN_CA@ -->
authors: Hazel Victoria Campbell
status: Published
summary: Lab Procedure, Lab Assignments, Lab Marking
----

[TOC]

# Description

In this lab you will make a JS Clock/Timer/Stopwatch/Countdown "single-page" app.
The app won't require any network traffic except loading a single HTML file.
You will use DHTML, promises, and async/await to connect your code and make sure each piece of code runs at the same time, and that the Clock, Timer, Stopwatch, and Countdown functions all work at the same time, independently.

<!-- ## Warning!

<p class="longWarning">
Due to the Thanksgiving holiday, there will be no walkthroughs for this lab. You will submit a single HTML file on eClass. Please ensure your code is well-commented so the TAs know that you understand your code. See the Heroku lab description for detailed examples of good vs bad comments.
</p> -->

## Learning Goals

* Basic DOM manipulation
* A thorough understanding of JS functions, methods, classes, and objects.
* Combining JS, HTML, and CSS into a single file.

# Getting Started

1. Create an HTML page: `clock.html`. This must contain all of your HTML, CSS and JS.

# App

## HTML

* Make sure your `<head>` has a title and specifies UTF-8 encoding.
* Create an element in `<head>` for all of your CSS code.
* Create an element in `<head>` for all of your JS code.
* Create a body with **semantic** HTML for four parts of the app: clock, timer, stopwatch, and countdown.

## JS

You should put your JS in head in a single element. You can either have it specify a ES module, or you can start your JS with `'use strict';`.

Make sure your JS doesn't try to do much before the page (and DOM) is finished loading! For example, you could create a `main` function and then have the browser call it when everything is loaded like this:

```js
window.addEventListener('load', main);
```
Keep in mind in the above example, `main` is a reference (pointer) to a
function or a method. **You should never pass JS code as a string!**

You should avoid using HTML attributes like `onload` or `onclick` to run JS code. Instead, use `addEventListener` like in the example above.

### Ticker Class

Using the *observer design pattern*, and the *singleton design pattern*, create a JS model class that allows other classes to register to be notified once a second.

You can do this using a `setTimeout` in order to update the page once a second. For the purposes of this exercise you are not allowed to use `setInterval`. In addition, you should only use `setTimeout` once, and you must make sure that only one timeout is running at a time!

The ticker class needs to run approximately once per second to update the page. **Do not update the page faster than twice per second, or slower than once every two seconds.**

Your Ticker class should contain:

* Code to make sure it is a singleton.
* `addObserver` and `notify` methods following the observer design pattern for observables.
* Exactly one call to `setTimeout`.
* Code to make sure the previous timeout is finished before starting the next Timeout.

Hints:

* Do not put the `setTimeout` in a loop.
* Remember the late-binding nature of JS.

## The Page

The page should have a title and four distinct areas. One area for the clock, one for the timer, one for the stopwatch, and one for the countdown.

Use CSS to make each area separate.

Hints:

* Semantic HTML elements like `<section>` and `<h2>` are appropriate for for each part of page!

## Clock

In the clock part of the page, there should be an appropriate element to show the current time. 

Create a `Clock` class, to put all your JS code for managing the `Clock`. Make sure it has an `update` method and adds itself an as observer to the `Ticker` class.

Every time `Ticker` notifies the `Clock`, use JS to update the element in the DOM to show the current time.

## Timer

* The timer should have two number inputs. One for minutes, and one for seconds. 
* There should also be a checkbox, that when checked, causes the timer to run, and when not checked, stops the timer.
* The timer should also be able to show "Timer stopped" when the timer is stopped.
* The timer should show "Time's Up!" when the timer is reaches 0 and hasn't been stopped yet.
* When the timer is running, you should disable the minutes and seconds inputs.
* Create a `Timer` class similar to the clock class, to hold all of your code for the timer, including manipulating the DOM.

## Stopwatch

* The stopwatch should have three buttons: Start, Stop, and Reset.
* When the stopwatch start button is clicked, the stopwatch should start.
* When the stopwatch is running, the start button should be disabled.
* When the stop button is clicked, the stop watch should **pause**.
* When the stop watch is **not** running, the stop button should be disabled.
* When the reset button is pressed, the stopwatch should start over from zero.
* The stopwatch should display the elapsed time in h:mm:ss.sss seconds, with hours, minutes, seconds, and .miliseconds.
    * If there's less than 10 minutes or seconds it should show the leading zero.
    * If there's less than 100 ms, it should also show the leading zeroes.

## Countdown

* The countdown timer should have a `datetime-local` input or a separate `date` input and `time` input to allow the user to pick the date and time they want to count down to.
* The countdown timer should show the years, months, days, hours, minutes, and seconds remaining until the date and time the user selected.
    * Example: "0 years 0 months 9 days 21 hours 24 minutes 32 seconds remaining"
* If the countdown time has already passed, the countdown timer should show the time since the date and time the user selected.
    * Example: "0 years 0 months 9 days 21 hours 24 minutes 32 seconds ago"
* A hidden element should appear when the countdown is over.
    * Make the element appear by changing the CSS styling of the element using JavaScript.

# Requirements

* Your CSS and HTML must pass validation: <https://validator.w3.org/nu/>
* Your JS, CSS, and HTML must not create any warnings or errors in Firefox Developer Edition.
* Your HTML should use the most appropriate semantic elements.
    * Your countdown should use a `datetime-local` input, or separate `date` and `time` inputs.
    * Your timer should use checkbox or radio buttons to allow pausing and unpausing.
    * Inputs should be appropriately labelled with label elements. [More info]()
    * It should be **obvious** what each input does.
    * The page should have a title and four distinct sections.
    * All CSS should be in a single element in head.
    * All JS should be in a single element in head.
        * Your HTML should **not** contain `style=` or `onload=` or similar attributes.
* Your JS should demonstrate an understanding JavaScript functions, anonymous functions, classes, binding, looping, and basic DOM manipulation.
    * You should use `setTimeout` **only once**.
    * Your JS should modify CSS styles to hide and unhide elements.
    * Your JS should modify the text inside elements.
    * Your JS should disable/enable elements.
    * You should never pass a string to an event handler, `setTimeout`, or other function that can take both a code string and a function reference.
    * Your JS contains a `Ticker` class that follows the singleton design pattern and the observer design pattern.
        * `Ticker` class should contain `addObserver` and `notify` methods, so it can be observable.
        * Attempting to instantiate multiple `Ticker` objects should fail with an error.
        * Your Ticker should update the page approximately once per second.
    * Your JS contain `Clock`, `Timer`, `Stopwatch`, and `Countdown` classes. These classes are entirely reponsible for managing their part of the application.
        * These four classes get called by `Ticker` approximately once per second to update the DOM.
* Your CSS should make your app aesthetically appealing.
    * It should look nice.
    * Every element should be readable.
    * It should be clear what every element does.
    * It should be **obvious** to anyone how to use all of the functions of the app.
    * Each part of the app should be separated, visually distinct, and titled.
    * Your CSS must make sure the element with the message about the countdown being over is hidden until the countdown is over.

# Restrictions

Violation of the restrictions will result a mark of zero.

* You **must not** use `setInterval` or `requestAnimationFrame`.
    * You may use `setTimeout` only once at a time.
        * You can call `setTimeout` multiple times.
        * However, you must wait until the previous timeout finishes, before calling it again.
        * You must **not** have multiple timeouts running at once.
        * It must be **obvious** in your code that multiple timeouts are never running at once.
* All JS and CSS are included in the single HTML file, `clock.html`
* Using of any frontend frameworks, CSS libraries, JS libraries or frameworks is forbidden. 
  * You must write plain JS, CSS and HTML. 
  * You must not use JS libraries, frameworks, preprocessors, or transpilers.
  * You must not use CSS libraries, frameworks, preprocessors or transpilers.
  * You must not use frontend frameworks, HTML frameworks, preprocessors or transpilers. 
* JS must `'use strict';` at the top, or it must be an ES Module.
* Nothing may be loaded by JS/HTML/CSS. (Network pane should only have one "GET clock.html" in it.)
* Must not contain any `<div>` or `<span>` elements.

# Submission Instructions

Upload your entire app as a single HTML file directly to Canvas.

# Collaboration

* You may consult with others (exchange high-level ideas) but the submission should be your own source code.
* Collaboration must be documented in your source code.
* Any source code you got from anywhere else must be cited in the source code. This includes code from LLMs.
* You can only use source code that **you understand**: see the [lab marking info]({filename}/general/labs.md#lab-marking)
* For more information see the collaboration section in the outline: [{filename}/general/outline.md#consultation-assignments-labs]

# Hints

For the countdown timer you can use an algorithm like this:

Imagine you have two datetimes a, and b. and a is less than b. Then we want to compute c = b - a

1. c's seconds = b's seconds - a's seconds
2. if c's seconds < 0, then borrow one minute from b, and increase c's seconds += 60
3. c's minutes = b's minutes - a's minutes
4. if c's minutes < 0, then borrow one hour from b, and increase c's minutes += 60
5. and so on...

The tricky one is the days, where you need to calculate how many days you borrowed:

1. c's days = b's days - a's days
2. if c's days < 0, then borrow one month from b and increase c's days += X where X = the # of days between the original value of b and the value of b after you borrowed a month


