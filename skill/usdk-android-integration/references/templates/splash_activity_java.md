# Splash Activity Template

Use this when the real launcher or splash activity should host USDK splash behavior.

## SDK-Hosted Consent Path

```java
package ${ACTIVITY_PACKAGE};

import android.app.Activity;
import android.content.Intent;
import com.herosdk.HeroSdk;
import com.herosdk.SdkSplashActivity;
import com.herosdk.listener.IProtocolListener;

public class ${SPLASH_CLASS} extends SdkSplashActivity {
    @Override
    public void onSplashStop() {
        startActivity(new Intent(this, ${NEXT_ACTIVITY}.class));
        finish();
    }

    @Override
    protected void onStart() {
        super.onStart();
        final Activity activity = this;
        HeroSdk.getInstance().setProtocolListener(new IProtocolListener() {
            @Override
            public void onAgree() {
                HeroSdk.getInstance().init(activity, "${PRODUCT_ID}", "${PRODUCT_KEY}");
            }
        });
    }
}
```

## Self-Hosted Consent Path

```java
package ${ACTIVITY_PACKAGE};

import android.content.Intent;
import com.herosdk.HeroSdk;
import com.herosdk.SdkSplashActivity;

public class ${SPLASH_CLASS} extends SdkSplashActivity {
    @Override
    public void onSplashStop() {
        startActivity(new Intent(this, ${NEXT_ACTIVITY}.class));
        finish();
    }

    private void onUserAcceptedProtocol() {
        HeroSdk.getInstance().setAgreeProtocol(this);
        HeroSdk.getInstance().init(this, "${PRODUCT_ID}", "${PRODUCT_KEY}");
    }
}
```

## Notes

- Choose exactly one consent path.
- Replace placeholder values with real inputs when available.
- If the project already has a launch flow, adapt it instead of duplicating navigation.
