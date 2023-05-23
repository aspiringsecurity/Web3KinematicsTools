# MUD boilerplate on Optimism for OP Kinematics

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

