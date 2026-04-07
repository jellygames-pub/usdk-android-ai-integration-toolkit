# Activity Lifecycle Forwarding Template

Use this when the main activity or integration wrapper must forward lifecycle callbacks into USDK.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    HeroSdk.getInstance().onCreate(this);
}

@Override
protected void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    HeroSdk.getInstance().onNewIntent(this, intent);
}

@Override
protected void onStart() {
    super.onStart();
    HeroSdk.getInstance().onStart(this);
}

@Override
protected void onResume() {
    super.onResume();
    HeroSdk.getInstance().onResume(this);
}

@Override
protected void onPause() {
    HeroSdk.getInstance().onPause(this);
    super.onPause();
}

@Override
protected void onStop() {
    HeroSdk.getInstance().onStop(this);
    super.onStop();
}

@Override
protected void onRestart() {
    super.onRestart();
    HeroSdk.getInstance().onRestart(this);
}

@Override
protected void onDestroy() {
    HeroSdk.getInstance().onDestroy(this);
    super.onDestroy();
}

@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    HeroSdk.getInstance().onActivityResult(this, requestCode, resultCode, data);
}

@Override
public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
    super.onRequestPermissionsResult(requestCode, permissions, grantResults);
    HeroSdk.getInstance().onRequestPermissionsResult(this, requestCode, permissions, grantResults);
}
```

## Notes

- Merge with the existing lifecycle logic instead of replacing it.
- Preserve project-specific side effects and call ordering where required.
