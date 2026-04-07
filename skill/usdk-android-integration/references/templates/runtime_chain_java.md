# Runtime Chain Template

Use this when wiring login, role upload, payment, logout, and exit into the real game flow.

```java
private RoleInfo buildRoleInfo() {
    RoleInfo roleInfo = new RoleInfo();
    roleInfo.setRoleId("${ROLE_ID}");
    roleInfo.setRoleName("${ROLE_NAME}");
    roleInfo.setServerId("${SERVER_ID}");
    roleInfo.setServerName("${SERVER_NAME}");
    roleInfo.setRoleLevel("${ROLE_LEVEL}");
    roleInfo.setVipLevel("${VIP_LEVEL}");
    roleInfo.setRoleBalance("${ROLE_BALANCE}");
    roleInfo.setPartyId("${PARTY_ID}");
    roleInfo.setPartyName("${PARTY_NAME}");
    roleInfo.setPartyRoleId("${PARTY_ROLE_ID}");
    roleInfo.setPartyRoleName("${PARTY_ROLE_NAME}");
    roleInfo.setProfessionId("${PROFESSION_ID}");
    roleInfo.setProfession("${PROFESSION_NAME}");
    roleInfo.setRoleGender("${ROLE_GENDER}");
    roleInfo.setRolePower("${ROLE_POWER}");
    roleInfo.setRoleCreateTime("${ROLE_CREATE_TIME}");
    roleInfo.setFriendList("${FRIEND_LIST}");
    roleInfo.setBalanceLevelOne(${BALANCE_LEVEL_ONE});
    roleInfo.setBalanceLevelTwo(${BALANCE_LEVEL_TWO});
    roleInfo.setSumPay(${SUM_PAY});
    return roleInfo;
}

private OrderInfo buildOrderInfo() {
    OrderInfo orderInfo = new OrderInfo();
    orderInfo.setGoodsId("${GOODS_ID}");
    orderInfo.setGoodsName("${GOODS_NAME}");
    orderInfo.setGoodsDesc("${GOODS_DESC}");
    orderInfo.setCpOrderId("${CP_ORDER_ID}");
    orderInfo.setSdkOrderId("${SDK_ORDER_ID}");
    orderInfo.setAmount(${AMOUNT});
    orderInfo.setCount(${COUNT});
    orderInfo.setPrice(${PRICE});
    orderInfo.setCallbackUrl("${CALLBACK_URL}");
    orderInfo.setServerMessage("${SERVER_MESSAGE}");
    orderInfo.setExtraParams("${EXTRA_PARAMS}");
    orderInfo.setGoodsType(${GOODS_TYPE});
    orderInfo.setCurrency("${CURRENCY}");
    orderInfo.setOriginJson("${ORIGIN_JSON}");
    return orderInfo;
}

private void triggerUsdkLogin() {
    HeroSdk.getInstance().login(this);
}

private void reportRoleEnterGame() {
    HeroSdk.getInstance().enterGame(this, buildRoleInfo());
}

private void reportCreateNewRole() {
    HeroSdk.getInstance().createNewRole(this, buildRoleInfo());
}

private void reportRoleLevelUp() {
    HeroSdk.getInstance().roleLevelUp(this, buildRoleInfo());
}

private void triggerUsdkPay() {
    HeroSdk.getInstance().pay(this, buildOrderInfo(), buildRoleInfo());
}

private void registerKickListener() {
    HeroSdk.getInstance().setKickListener(new IKickListener() {
        @Override
        public void onKick(int code, String message) {
            // Route this into the real relogin, title-screen, or forced-exit flow.
        }
    });
}

private void triggerUsdkLogout() {
    HeroSdk.getInstance().logout(this);
}

private void triggerUsdkExit() {
    if (Boolean.TRUE.equals(HeroSdk.getInstance().isChannelHasExitDialog())) {
        HeroSdk.getInstance().exit(this);
        return;
    }

    // Show the game's own confirm dialog first when the channel does not provide one.
    HeroSdk.getInstance().exit(this);
}
```

## Notes

- Do not call all of these in `onCreate()` unless the game actually works that way.
- Bind each method to the real game event that owns it.
- `pay` should be attached to the real purchase action, not a startup placeholder.
- Replace the sample `OrderInfo` placeholders with real goods, amount, callback, and server-side correlation data before runtime acceptance.
- `enterGame` should happen only after login succeeds and the role is known.
- `createNewRole` must be attached to the real role-creation event.
- `roleLevelUp` must be attached to the real level-up event.
- Replace the sample `RoleInfo` placeholders with real game data before runtime acceptance.
- Register `setKickListener` before runtime entry points that may receive SDK callbacks.
- Route the game exit button and the back key through the same exit decision path.
- Check `isChannelHasExitDialog()` before deciding whether the game should show its own exit confirmation UI.
