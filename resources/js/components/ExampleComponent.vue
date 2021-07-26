<template>
    <div class="container bg-gray-100 dark:bg-gray-900">
        <div class="row justify-content-center">
            <button class="btn btn-primary" @click="throwException">
                Nothing happens. Guaranteed!
            </button>
            <button class="btn btn-primary ml-2" @click="logMessage">
                Slide Into DMs
            </button>
            <button class="btn btn-primary ml-2" @click="justSomeCrumbs">
                Leave a Trail
            </button>
        </div>
    </div>
</template>

<script>
import * as Sentry from "@sentry/vue";

export default {
    mounted() {
        console.log("Component mounted.");
    },
    methods: {
        throwException() {
            try {
                throw new Error("Not reachable.");
            } catch (err) {
                Sentry.captureException(err);
            }
        },
        logMessage() {
            Sentry.captureMessage("This is a message");
        },
        justSomeCrumbs() {
            Sentry.addBreadcrumb({
                category: "category",
                message: "Test Breadcrumb",
                level: Sentry.Severity.Info
            });
            try {
                throw new Error("Is there a trail.");
            } catch (err) {
                Sentry.captureException(err);
            }
        }
    }
};
</script>
