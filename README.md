# Grandma
A silly bot for discord, now public!

## Usage

Either:
- Run as a docker container from `laura7089/grandma_bot`
- Run from the command line, with `main.py`:
`python3 main.py [optional args]`

## Passing ClientID

The recommended method of passing client ID of your bot's discord account is via an environment variable (named `CLIENT_ID`), alternatively, you can pass it via an argument but beware as **this will store the plaintext ID in your shell's history**.

## Custom Responses

Insert all your response files as `.yaml` files in `custom-responses` or with a docker image mount a volume in `/app/custom-responses`.
To add a response, add the message text as a top-level header, then add *two* responses underneath, one for grandmarating and one for grandmalevel (leave one blank if not desired).
