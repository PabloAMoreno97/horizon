<script lang="ts">
export default {
    data() {
        return {
            firstName: "Pablo",
            userCity: "Envigado",
            userZipCode: "055422",
            articleTypesList: ["class1", "class2", "class3", "class4"]
        }
    },
}
</script>

<template>
    <div class="header">
        <div>
            <span>
                |||
                <img src="" alt="Horizon">
            </span>
            <span>
                <span>{{ firstName }}</span>
                <span>|||</span>
                <span>(chart icon)</span>
            </span>
        </div>
        <div>
            <form>
                <input type="text" name="" id="">
                <button>(Icono)</button>
            </form>
        </div>
        <div>
            <span v-for="(articleType, index) in articleTypesList">{{ articleType }}</span>
        </div>
        <div class="header-addres">
            <span>Deliver to {{ firstName }} - {{ userCity }} {{ userZipCode }}</span>
        </div>
    </div>
</template>

<style scoped>
.header {
    background-color: rgb(35, 35, 46);
    color: white;
    display: flex;
    flex-direction: column;
}

.header-addres {
    background-color: rgb(73, 73, 82);
    color: white
}

.header div {
    display: flex;
    justify-content: space-between;
}
</style>