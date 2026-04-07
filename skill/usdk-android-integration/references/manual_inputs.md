# Manual Inputs

These items are external to static code integration and should be surfaced clearly instead of guessed.

## Provider-Side Inputs

- `productId`
- `productKey`
- SDK package variant choice: `android` or `androidx`
- Protocol mode choice:
  - `USDK protocol popup`
  - `Game-owned protocol popup`
- Payment callback URL
- Payment callback signing key
- Goods and pricing configuration in the provider console
- Test account or sandbox account setup

## Integrator Decisions

- Which `Application` class should own USDK initialization
- Which launch or splash activity should host `SdkSplashActivity`
- Which protocol mode is selected for this integration
- Which post-login point should trigger `enterGame`
- Which purchase flow should call `pay`
- Whether optional extension modules are in scope

## Strong Reminders

- `exit` integration is not a standalone branch choice.
- AI should explicitly remind the integrator to review whether the channel provides its own exit dialog.
- AI should explicitly remind the integrator to review whether the game needs a local confirmation dialog when the channel does not provide one.
- AI should explicitly remind the integrator to route the correct in-game actions through the shared exit path, including the back key when applicable.

## Completion Rule

If any item above is missing, the engineering integration can still be scaffolded, but the final report must mark the integration as `blocked_on_manual_inputs` rather than `done`.
