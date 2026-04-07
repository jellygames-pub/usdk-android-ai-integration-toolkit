package com.example.usdkfixture;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
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
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        final Activity activity = this;
        HeroSdk.getInstance().setProtocolListener(new IProtocolListener() {
            @Override
            public void onAgree() {
                HeroSdk.getInstance().init(activity, "productId", "productKey");
            }
        });
    }
}
