# Gradle Template For AndroidX Projects

Use this when `gradle_sdk_variant_detected = androidx`.

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
    implementation 'androidx.legacy:legacy-support-v4:1.0.0'
    implementation 'androidx.multidex:multidex:2.0.1'
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
    implementation 'androidx.legacy:legacy-support-v4:1.0.0'
    implementation 'androidx.multidex:multidex:2.0.1'
    implementation(name: 'HeroUSDK', ext: 'aar')
}
```

## Notes

- For Gradle 7+ projects with `FAIL_ON_PROJECT_REPOS` or `PREFER_SETTINGS`, do not add `flatDir` in `app/build.gradle`.
- Keep existing dependencies intact.
- If the project already declares AndroidX support libs elsewhere, avoid duplicate declarations.
