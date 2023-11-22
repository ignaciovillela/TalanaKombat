# Talana Kombat JRPG

Talana Kombat JRPG is a text-based fighting game where two characters face each other in a battle to the death. Each character has unique special moves, and the outcome of the fight is determined by the sequence of movements and hits performed by the players.

## Getting Started

Follow the instructions below to set up and run Talana Kombat JRPG.

### Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Installation

1. Clone the repository:

    ```bash 
   git clone https://github.com/your_username/talanakombat.git
    ```

2. Navigate to the project directory:

    ```bash
    cd talanakombat
    ```

3. Build the Docker image:

    ```bash
    docker-compose build
    ```

## Usage

1. Run the Docker container:

    ```bash
    docker-compose up
    ```

2. Use Postman or a similar tool to interact with the Talana Kombat JRPG API. Send POST requests to [http://localhost:8000/kombat/fight](http://localhost:8000/kombat/fight) with the fight data in the request body.

    Example JSON for the fight data:

    ```json
    {
        "player1": {
            "movements": ["D", "DSD", "S", "DSD", "SD"],
            "hits": ["K", "P", "", "K", "P"]
        },
        "player2": {
            "movements": ["SA", "SA", "SA", "ASA", "SA"],
            "hits": ["K", "", "K", "P", "P"]
        }
    }
    ```

    This will simulate a fight and return the narrative of the battle.

Feel free to customize the movements and hits for each player according to your preferences.
