package com.example.partialfixture;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import com.herosdk.HeroSdk;
import com.herosdk.bean.OrderInfo;
import com.herosdk.bean.RoleInfo;

public class MainActivity extends Activity {
    private RoleInfo buildRoleInfo() {
        RoleInfo roleInfo = new RoleInfo();
        roleInfo.setRoleId("2001");
        roleInfo.setRoleName("partial-role");
        roleInfo.setServerId("2");
        roleInfo.setServerName("partial-server");
        roleInfo.setRoleLevel("1");
        roleInfo.setVipLevel("0");
        return roleInfo;
    }

    private OrderInfo buildOrderInfo() {
        OrderInfo orderInfo = new OrderInfo();
        orderInfo.setGoodsId("goods_partial_1");
        orderInfo.setCpOrderId("cp_order_partial_1");
        return orderInfo;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        HeroSdk.getInstance().onCreate(this);
        HeroSdk.getInstance().login(this);
        HeroSdk.getInstance().enterGame(this, buildRoleInfo());
        HeroSdk.getInstance().pay(this, buildOrderInfo(), buildRoleInfo());
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
        HeroSdk.getInstance().logout(this);
        HeroSdk.getInstance().exit(this);
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
}
