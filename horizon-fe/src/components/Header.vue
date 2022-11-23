<script lang="ts">

export default {
    data() {
        return {
            firstName: "pablo",
            userCity: "Envigado",
            userZipCode: "055422",
            articleTypesList: ["class1", "class2", "class3", "class4", "class5", "class6", "class7", "class8", "class9", "class10", "class11"]
        }
    },
}
</script>

<template>
    <div class="header">
        <div class="header-firstLine">
            <span>
                <font-awesome-icon icon="fa-solid fa-bars" />
                <a href="#">
                    <img src="../assets/logo_horizon.png" alt="Horizon" class="header-logo__img">
                </a>
            </span>
            <span>
                <span>{{ firstName }}</span>
                <span>
                    <font-awesome-icon icon="fa-regular fa-user" />
                    <font-awesome-icon icon="fa-solid fa-cart-shopping" />
                </span>
            </span>
        </div>
        <div class="header-secondLine">
            <form>
                <input type="text" name="" id="" placeholder="Search Horizon">
                <button>
                    <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
                </button>
            </form>
        </div>
        <div class="header-articleTypes">
            <span v-for="(articleType, index) in articleTypesList">
                {{ articleType }}
            </span>
        </div>
        <div class="header-addres">
            <span>
                <font-awesome-icon icon="fa-solid fa-location-dot" />Deliver to {{ firstName }} - {{ userCity }} {{
        userZipCode
                }}
            </span>
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

.header-logo__img {
    width: 2.5rem;
    height: 1.7rem;
}

.header-articleTypes {
    overflow-x: auto;
    scrollbar-width: none;
}

.header-articleTypes::-webkit-scrollbar {
    width: 0;
}

.header-firstLine span {
    align-items: center;
}
</style>