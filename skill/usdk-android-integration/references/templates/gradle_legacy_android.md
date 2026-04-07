# Gradle Template For Legacy Android Support Projects

Use this when `gradle_sdk_variant_detected = android`.

## Gradle 7+ With Settings-Managed Repositories

Put the repository declaration in `settings.gradle` or `settings.gradle.kts`:

```gradle
dependencyResolutionManagement {
    repositories {
        google()
        mavenCentral()
        flatDir {
            dirs "${rootDir}/app/libs"
        }
    }
}
```

Keep the dependency declaration in `app/build.gradle`:

```gradle
dependencies {
    implementation files('libs/android-support-multidex.jar')
    implementation files('libs/android-support-v4.jar')
    implementation(name: 'HeroUSDK', ext: 'aar')
}
```

## Gradle 7 Below Or Project-Managed Repositories

```gradle
android {
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }

    repositories {
        flatDir {
            dirs 'libs'
        }
    }
}

dependencies {
    implementation files('libs/android-support-multidex.jar')
    implementation files('libs/android-support-v4.jar')
    implementation(name: 'HeroUSDK', ext: 'aar')
}
```

## Notes

- For Gradle 7+ projects with `FAIL_ON_PROJECT_REPOS` or `PREFER_SETTINGS`, do not add `flatDir` in `app/build.gradle`.
- Use this only for legacy support projects.
- Do not mix this path with AndroidX dependencies unless you are doing a deliberate migration.
