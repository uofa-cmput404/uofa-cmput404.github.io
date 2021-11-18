Title: Lab 8 - WebSockets
Date: 2019-02-19 13:35
Modified: 2019-02-20 15:03
Category: Lab
Tags: nodejs, websockets
Authors: Alexander Wong

----

Learn how to utilize [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) and [Phaser.io](https://phaser.io/). Create a basic Phaser game with WebSocket connectivity for real-time server to client communication. Use [Node.js](https://nodejs.org/en/) for our application server. Use [TypeScript](https://www.typescriptlang.org/) with [Parcel](https://parceljs.org/) for bundling browser client code.

### Install Node.js

There are two different ways you can try to install node.js!

#### Option 1: Install node on my own computer

If you don't already have node.js installed, 
download and install node from the node from the 
[node.js website](https://nodejs.org/en/download/).

This won't be possible on the lab machines, because it requires 
administrator/root.

If you already have node installed, please check the version with `node -v`.

Example:

```bash
$ node -v
v15.11.0
```

Make sure the version number is greater than 8! (In this case it's 15, which
is fine.)

If your version is older than 8, please either uninstall node and reinstall
a more recent version of node from the 
[node.js website](https://nodejs.org/en/download/) or follow the instructions
in the next section for the lab machines and VM.

#### Option 2: Install Node with NVM

NVM allows you to install multiple versions of node on Linux or Macs
without being an administrator or root user.

NVM does not work on windows.

Install [Node Version Manager](https://github.com/nvm-sh/nvm). 

```bash
# curl
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash

# or wget
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
```

Close and reopen your terminal, or load nvm manually.
```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

Install the latest release of node.
```bash
nvm install node # latest node version

# LTS. Alternatively 8.15.0 (6.X is EOL April 2019)
# nvm install 10.15.1 
```

Map this version of node as the current default.
```bash
nvm alias default node
node --version
# v11.10.0
npm --version
# 6.7.0
```
### Initialize Phaser and WebSockerServer

Fork this repository and clone it locally onto your own machine.

* [github.com/uofa-cmput404/nodejs-ws-lab](https://github.com/uofa-cmput404/nodejs-ws-lab)

Run the application locally, following the quickstart instructions.

```bash
npm install
npm start
# navigating to browser, localhost:8080
```

You can ignore warnings/errors about security vulnerabilities.

If you get errors after `npm install` on Mac OS, look for an error about Xcode.
If there is an error about Xcode, you may need to install it: [Xcode](https://developer.apple.com/xcode/).

If you get the error `Cannot find module 'ws'` after running `npm start`, try downgrading your node version with `npm install 10.15.1` OR `nvm install 10.15.1`
(depending on which node manager you're using). 

If there is an error like `favicon.ico: Invalid Version: undefined` 
this is because of a bug in parcel bundler 1.12.4, so downgrade to 1.12.3 by
running `npm install parcel-bundler@1.12.3`.

**Question 1**: What do you see in the browser? When you open another tab and perform a click/drag action, what happens?

**Question 2**: What are some of the differences between TypeScript and JavaScript?

**Question 3**: Why is a web application bundler (Parcel, Webpack, Rollup, etc.) useful for modern web projects? What are some features that [ParcelJS](https://parceljs.org/) provides?

### Top Down Scroller

We will now utilize the other assets and create a top down game where we control our character using the arrow keys.

Checkout the [`topdown`](https://github.com/uofa-cmput404/nodejs-ws-lab/tree/topdown) branch from GitHub and make note of the changes in `client.ts`.

```bash
git remote -v # show your current remotes
git remote add laborigin https://github.com/uofa-cmput404/nodejs-ws-lab.git
git fetch laborigin
git checkout -b topdown laborigin/topdown
```

Within `client.ts` the `preload` function is now loading our required assets. The `create` function has been updated to use our tilemap data, spritesheet, and character assets. Additional logic for handling animations and keyboard input has also been added. An `update` function has been added to handle input logic and playing our sprite animations.

### Multiplayer Top Down Scroller

The `init` function will require modifications to work with multiple players.

Add a function that generates UUIDs before the Scene class. For this toy example, the following modified from [github gist](https://gist.github.com/jed/982883) is acceptable:

```typescript
function uuid(
  a?: any               // placeholder
): string {
  return a              // if the placeholder was passed, return
    ? (                 // a random number from 0 to 15
      a ^               // unless b is 8,
      Math.random()     // in which case
      * 16              // a random number from
      >> a / 4          // 8 to 11
    ).toString(16)      // in hexadecimal
    : (                 // or otherwise a concatenated string:
      1e7.toString() +  // 10000000 +
      -1e3 +            // -1000 +
      -4e3 +            // -4000 +
      -8e3 +            // -80000000 +
      -1e11             // -100000000000,
    ).replace(          // replacing
      /[018]/g,         // zeroes, ones, and eights with
      uuid              // random hex digits
    )
}
```

Initialize the ID as a class property, before the constructor. Add a `players` map object and refactor all references to `player` such that the map is now used instead.

```typescript
class GameScene extends Phaser.Scene {

  private VELOCITY = 100;
  private wsClient?: WebSocket;

  // delete this
  // private player?: Phaser.GameObjects.Sprite;
  // ...

  private id = uuid();
  private players: {[key: string]: Phaser.GameObjects.Sprite} = {};

  // ...

// Refactor your code such that all references to this.player
// becomes this.players[this.id]

// create
public create() {
  // ...
  this.players[this.id] = this.physics.add.sprite(48, 48, "player", 1);
  this.physics.add.collider(this.players[this.id], layer);
  this.cameras.main.startFollow(this.players[this.id]);
}


// update
public update() {
  if (this.players[this.id]) {
    const player = this.players[this.id];
    let moving = false;

    if (this.leftKey && this.leftKey.isDown) {
      (player.body as Phaser.Physics.Arcade.Body).setVelocityX(-this.VELOCITY);
      player.play("left", true);
      moving = true;
    }
    // ...
    player.update();
  }
}
```

Modify the `update` function to broadcast our player's position during movement.

```typescript
if (!moving) {
  (player.body as Phaser.Physics.Arcade.Body).setVelocity(0);
  player.anims.stop();
} else if (this.wsClient) {
  this.wsClient.send(JSON.stringify({
    id: this.id,
    x: player.x,
    y: player.y,
    frame: player.frame.name
  }));
}
```

Within `server.js`, change the WebSocket server message handler to accomodate a map of IDs and positions.

```javascript
function setupWSServer(server) {
  // ...
  let actorCoordinates = { };
  wss.on("connection", (ws) => {
    ws.on("message", (rawMsg) => {
      console.log(`RECV: ${rawMsg}`);
      const incommingMessage = JSON.parse(rawMsg);
      actorCoordinates[incommingMessage.id] = {
        x: incommingMessage.x,
        y: incommingMessage.y,
        frame: incommingMessage.frame
      }
    // ...
```

Update the `client.ts` file to handle the new map of positions, rendering multiple characters on screen.

The `ICoords` interface must change to accomodate a map of Ids to coordinates and frame numbers.

```typescript
interface ICoords {
  [key: string]: {
    x: number;
    y: number;
    frame: number;
  }
}
```

The websocket client should parse and store sprite objects received from the server.

```typescript
public init() {
  // ...
  this.wsClient.onmessage = (wsMsgEvent) => {
    const allCoords: ICoords = JSON.parse(wsMsgEvent.data);
    for (const playerId of Object.keys(allCoords)) {
      if (playerId === this.id) {
        // we don't need to update ourselves
        continue;
      }
      const { x, y, frame } = allCoords[playerId];
      if (playerId in this.players) {
        // We have seen this player before, update it!
        const player = this.players[playerId];
        if (player.texture.key === "__MISSING") {
          // Player was instantiated before texture was ready, reinstantiate
          player.destroy();
          this.players[playerId] = this.add.sprite(x, y, "player", frame);
        } else {
          player.setX(x);
          player.setY(y);
          player.setFrame(frame);  
        }
      } else {
        // We have not seen this player before, create it!
        this.players[playerId] = this.add.sprite(x, y, "player", frame);
      }
    }
  }
}
```

Let's modify our `update` function to also render all of the other players.

```typescript
public update() {
  for (const playerId of Object.keys(this.players)) {
    const player = this.players[playerId];

    if (playerId !== this.id) {
      player.setTint(0x0000aa); // so we can tell our guy apart
      player.update();
      continue;
    }
    // rest of the input handling code
```

The reference source code is available on the [finishedLab](https://github.com/uofa-cmput404/nodejs-ws-lab/tree/finishedLab) branch. You should now have a game running in your browser that handles real-time concurrent connections and updates among multiple users!

**Question 4**: What are the different values for the `readyState` a WebSocket can be in? Briefly describe what each state means. (Hint: check out the [Mozilla WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket))

**Question 5**: What's the link to your github repo?

Hint: `git push -u origin topdown:master`
