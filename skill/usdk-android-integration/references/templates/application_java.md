# Application Template

Use this when the project already has or needs a custom `Application` class.

```java
package ${APPLICATION_PACKAGE};

import com.herosdk.SdkApplication;

public class ${APPLICATION_CLASS} extends SdkApplication {
    @Override
    public void onCreate() {
        super.onCreate();

        // Keep existing app initialization below this line.
        ${EXISTING_ONCREATE_BODY}
    }
}
```

## Notes

- Prefer adapting the existing `Application` class instead of creating a second one.
- If there is existing initialization code, preserve it.
- Pair this template with a manifest update:

```xml
<application
    android:name=".${APPLICATION_CLASS}"
    ... />
```
