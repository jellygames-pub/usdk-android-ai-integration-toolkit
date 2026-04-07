package com.example.partialfixture;

import android.app.Activity;
import android.content.Intent;
import com.herosdk.HeroSdk;
import com.herosdk.SdkSplashActivity;
import com.herosdk.listener.IProtocolListener;

public class SplashActivity extends SdkSplashActivity {
    @Override
    public void onSplashStop() {
        startActivity(new Intent(this, MainActivity.class));
        finish();
    }

    @Override
    protected void onStart() {
        super.onStart();
        final Activity activity = this;
        HeroSdk.getInstance().setProtocolListener(new IProtocolListener() {
            @Override
            public void onAgree() {
                HeroSdk.getInstance().init(activity, "productId", "productKey");
            }
        });
    }
}
