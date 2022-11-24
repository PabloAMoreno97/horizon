<script lang="ts">

import LeftSideBar from './LeftSideBar.vue';

export default {

    data() {
        return {
            firstName: "pablo",
            userCity: "Envigado",
            userZipCode: "055422",
            articleTypesList: ["Deals", "Horizon Basic", "Buy Again", "Video", "Best Sellers", "Livestreams", "Books", "Home", "New Releases", "Gift Cards", "Health & Household"],
        }
    },
}
</script>

<template>

    <div class="header">
        <div class="header-firstLine">
            <span>
                <a href="#">
                    <LeftSideBar></LeftSideBar>
                    <img src="../assets/logo_horizon.png" alt="Horizon" class="header-logo__img">
                </a>
            </span>
            <span>
                <span>{{ firstName }} </span>
                <span>
                    <font-awesome-icon icon="fa-regular fa-user" class="header-userIcon" />
                    <font-awesome-icon icon="fa-solid fa-cart-shopping" class="header-cartIcon" />
                </span>
            </span>
        </div>
        <div class="header-secondLine">
            <form class="header-searchBar">
                <input type="text" name="" id="" placeholder="Search Horizon" class="header-searchBar__input">
                <button class="header-searchBar__button">
                    <font-awesome-icon icon="fa-solid fa-magnifying-glass" class="header-glassIcon" />
                </button>
            </form>
        </div>
        <div class="header-articleTypes">
            <span v-for="(articleType, index) in articleTypesList">
                <a href="#">{{ articleType }}</a>
            </span>
        </div>
        <div class="header-address">
            <span>
                <font-awesome-icon icon="fa-solid fa-location-dot" /> Deliver to {{ firstName }} - {{ userCity }} {{
        userZipCode
                }}
            </span>
        </div>
    </div>

</template>

<style scoped>
a {
    text-decoration: none;
}

.header {
    background-color: rgb(35, 35, 46);
    color: white;
    display: flex;
    flex-direction: column;
}

.header-address {
    background-color: rgb(73, 73, 82);
    padding: 0.5rem 0.7rem;
    color: white;
    font-size: 0.8rem;
}

.header div {
    display: flex;
    justify-content: space-between;
    padding-left: .7rem;
    padding-right: .7rem;
}

.header-logo__img {
    width: 3rem;
    height: 1.7rem;
}

.header-articleTypes {
    overflow-x: scroll;
    scrollbar-width: none;
    margin-top: 0.5rem;
    height: 2.5rem;
}

.header-articleTypes::-webkit-scrollbar {
    width: 0;
}

.header-articleTypes span {
    margin-right: 1rem;
}

.header-articleTypes span a {
    color: white;
    white-space: nowrap;
}

.header-firstLine {
    align-items: center;
}

.header-firstLine span {
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
    display: flex;
}

.header-secondLine form {
    display: flex;
    justify-content: space-between;
}

.header-bars {
    font-size: 1.6rem;
    margin-right: 0.7rem;
}

.header-userIcon,
.header-cartIcon {
    margin-left: 0.5rem;
    font-size: 1.6rem;
}

.header-searchBar {
    background-color: white;
    border: none;
    border-radius: 1.5rem;
    width: 100%;
    height: 2.5rem;
}

.header-searchBar__input {
    border: none;
    border-radius: 0.4rem;
    padding-left: 0.5rem;
    width: 100%;
    outline: none;
}

.header-searchBar__button {
    border: none;
    border-radius: 0.4rem;
    background-color: rgb(247, 176, 91);
    width: 3rem;
}

.header-glassIcon {
    font-size: 1.4rem;
}
</style>