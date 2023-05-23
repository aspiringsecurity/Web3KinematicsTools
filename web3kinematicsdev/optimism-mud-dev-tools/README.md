
## Why MUD?

MUD takes care of all the plumbing of building blockchain-based applications so you can focus on your application logic. In the MUD builders' own words:

> MUD is a framework for ambitious Ethereum applications. It compresses the complexity of building EVM apps with a tightly integrated software stack.

Go take a deep dive at [mud.dev](https://mud.dev/)! You'll be as excited as we are.

[![MUD 101](https://img.youtube.com/vi/IjxzJjJJSs8/0.jpg)](https://www.youtube.com/watch?v=IjxzJjJJSs8)

## Getting Started

### Install Node 18

[See here](https://nodejs.org/en/download/).

### Install Foundry

You will need to install [Foundry](https://book.getfoundry.sh/getting-started/installation) to build your smart contracts.

1. Run the following command:

   ```sh
   curl -L https://foundry.paradigm.xyz | bash
   ```

1. Source your environment as requested by Foundry.

1. Run `foundryup`.

</details>

### Install pnpm

Pnpm is the package manager MUD uses. It's usage is very similar to NPM but speed is much faster

```bash
npm install pnpm --global
```

## Start the application

1. Clone/fork the optimism-mud-starter repo

   ```sh
   git clone https://github.com/ethereum-optimism/optimism-mud-starter.git
   ```

2. Install the necessary node packages:

   ```sh
   cd optimism-mud-starter
   pnpm install
   ```

3. Initialize the mud project

   ```sh
   pnpm initialize
   ```

   If you get errors during this step, you might need to [update your Foundry to the latest version](#install-foundry).

4. Start dev server

```sh
pnpm dev
```

5. Open [localhost:3000](http://localhost:3000) in your browser.

