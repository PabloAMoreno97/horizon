<script lang="ts">
import type { faLandMineOn } from '@fortawesome/free-solid-svg-icons';


export default {

    data() {
        return {
            firstName: "pablo",
            userCity: "Envigado",
            userZipCode: "055422",
            browse: false,
            yourAccount: false,
            itemsInCart: 3,
            country: "United States",
            flag: "fa-solid fa-flag-usa",
            language: "English",
            currency: "$ - USD - US Dollar",
            articleTypesList: ["Deals", "Horizon Basic", "Buy Again", "Video", "Best Sellers", "Livestreams", "Books", "Home", "New Releases", "Gift Cards", "Health & Household"],
            trendingSection: 'Movers & Shakers',
            topDepartments: ['Home', 'Health & Household', 'Books', 'PC'],
            departments: ['HoliDeals', 'Horizon Music', 'Horizon Video', 'Books', 'Horizon Custom', 'Horizon Discover', 'Horizon Explore', 'Horizon Launchpad']
        }
    },
}
</script>

<template>
    <v-card>
        <header>
            <div class="header">
                <div class="header-firstLine">
                    <span>
                        <v-layout id="leftSideBarButton">

                            <v-navigation-drawer v-model="browse" temporary>
                                <section class="leftNav-header">
                                    <div id="leftNav-account">
                                        <v-btn color="transparent"
                                            @click.stop="(yourAccount = !yourAccount) && (browse = false)">
                                            <p>Your Account </p>
                                            <font-awesome-icon icon="fa-regular fa-user" class="header-userIcon" />
                                        </v-btn>
                                    </div>
                                    <div class="leftNav-title">
                                        <h3>Browse</h3>
                                        <h2>Horizon</h2>
                                    </div>
                                </section>
                                <section class="leftNav-homeContainer">
                                    <a href="/" class="leftNav-home">
                                        <span>Horizon Home</span>
                                        <span><font-awesome-icon icon="fa-solid fa-home" /></span>
                                    </a>
                                </section>
                                <section class="leftNav-trending">
                                    <h3>Trending</h3>
                                    <p> <a href="">{{ trendingSection }}</a> </p>
                                </section>
                                <section class="leftNav-departments">
                                    <h3>Top Departments</h3>
                                    <ul>
                                        <li v-for="topDepartment in topDepartments">
                                            <a href="">{{ topDepartment }}</a>
                                        </li>
                                        <li>
                                            <v-list-group>
                                                <template v-slot:activator>
                                                    <v-list-item-content>
                                                        <v-list-item-title>See All</v-list-item-title>
                                                    </v-list-item-content>
                                                </template>
                                                <v-list-item v-for="(department, i) in departments" :key="i" link>
                                                    <v-list-item v-text="department"></v-list-item>
                                                </v-list-item>
                                            </v-list-group>
                                        </li>
                                    </ul>
                                </section>
                            </v-navigation-drawer>

                            <div>
                                <v-btn color="transparent" @click.stop="(browse = !browse) && (yourAccount = false)">
                                    <font-awesome-icon icon="fa-solid fa-bars" class="header-bars" />
                                </v-btn>
                            </div>

                        </v-layout>
                        <a href="#">
                            <img src="../assets/logo_horizon.png" alt="Horizon" class="header-logo__img">
                        </a>
                    </span>
                    <span>
                        <span>
                            <v-layout id="rightSideBarButton">
                                <v-navigation-drawer v-model="yourAccount" location="right" temporary>
                                    <section class="rightNav-header">
                                        <div id="rightNav-browse">
                                            <v-btn color="transparent"
                                                @click.stop="(browse = !browse) && (yourAccount = false)">
                                                <span class="rightNav-browse__text">Browse</span>
                                                <span><font-awesome-icon icon="fa-solid fa-bars"
                                                        class="rightNav-browse__icon" /></span>
                                            </v-btn>
                                        </div>
                                        <div class="rightNav-title">
                                            <h3>Hello, {{ firstName }}</h3>
                                            <h2>Your Account</h2>
                                        </div>
                                    </section>
                                </v-navigation-drawer>
                                <v-btn color="transparent"
                                    @click.stop="(yourAccount = !yourAccount) && (browse = false)">
                                    <span>{{ firstName }} > </span>
                                    <font-awesome-icon icon="fa-regular fa-user" class="header-userIcon" />
                                </v-btn>
                            </v-layout>
                            <p class="header-itemsInCart">{{ itemsInCart }}</p>
                            <a href="#" class="header-cartIcon__a">
                                <font-awesome-icon icon="fa-solid fa-cart-shopping" class="header-cartIcon" />
                            </a>
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
                        <font-awesome-icon icon="fa-solid fa-location-dot" /> Deliver to {{ firstName }} - {{ userCity
                        }} {{
        userZipCode
}}
                    </span>
                </div>
            </div>
        </header>

        <main>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque, error molestias velit ab praesentium
            doloribus quas ea provident voluptate quod labore sequi nostrum! Iure ab vitae vero porro, quidem iusto.
        </main>

        <footer>
            <section class="footer">
                <div class="footer-topPage">
                    <p><font-awesome-icon icon="fa-solid fa-arrow-circle-up" /></p>
                    <p>top page</p>
                </div>
                <ul class="footer-sectionsList">
                    <li><a href="#">Amazon.com</a></li>
                    <li><a href="#">Your Orders</a></li>
                    <li><a href="#">Your List</a></li>
                    <li><a href="#">Gift Cards & Registry</a></li>
                    <li><a href="#">Find a Gift</a></li>
                    <li><a href="#">Your Account</a></li>
                    <li><a href="#">Your Subscribe & Save</a></li>
                    <li><a href="#">Browsing History</a></li>
                    <li><a href="#">Sell products on Horizon</a></li>
                    <li><a href="#">Your Recommendations</a></li>
                    <li><a href="#">Returns</a></li>
                    <li><a href="#">1-Click Settings</a></li>
                    <li><a href="#">Customer Service</a></li>
                    <li><a href="#">Your Recalls</a></li>
                    <li><a href="#">Help</a></li>
                </ul>
            </section>
            <section class="footer-account">
                <div class="footer-settingsContainer">
                    <span><font-awesome-icon icon="fa-solid fa-globe" /> {{ language }}</span>
                    <span>{{ currency }}</span>
                    <span>
                        <font-awesome-icon :icon="flag" /> {{ country }}
                    </span>
                </div>
                <a href="#">Switch Accounts</a>
                <a href="#">Sign Out</a>
                <div class="footer-useConditions">
                    <span>Conditions of User</span>
                    <span class="footer-useConditions__span2">Privacy Notice</span>
                    <span>Interested-Based Ads</span>
                </div>
                <p class="footer-rights">© 1996-2022, Horizon.com, Inc. or its affiliates</p>
            </section>
        </footer>
    </v-card>

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
}

#leftSideBarButton {
    overflow: hidden;
    width: 3rem;
}

#rightSideBarButton {
    overflow: hidden;
}

.header-logo__img {
    width: 5rem;
    height: 2rem;
}

.header-articleTypes {
    overflow-x: scroll;
    scrollbar-width: none;
    margin-top: 0.5rem;
    height: 2.5rem;
    padding-left: 0.7rem;
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
    padding-right: 0.7rem;
}

.header-firstLine span {
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
}

.header-secondLine {
    padding-left: 0.7rem;
    padding-right: 0.7rem;
}

.header-secondLine form {
    display: flex;
    justify-content: space-between;
}

.header-bars {
    font-size: 1.6rem;
    margin-right: 0.7rem;
}

.header-userIcon {
    font-size: 1.6rem;
}

.header-cartIcon {
    font-size: 1.6rem;
    z-index: 50;
}

.header-cartIcon__a {
    color: white;
}

.header-itemsInCart {
    position: absolute;
    right: 1.2rem;
    top: 1.05rem;
    color: rgb(187, 21, 21);
    font-size: 0.9rem;
    font-weight: 600;
    z-index: 100;
}

.header-searchBar {
    background-color: white;
    border: none;
    border-radius: 0.5rem;
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
    background-color: rgb(218, 47, 47);
    width: 3rem;
}

.header-glassIcon {
    font-size: 1.4rem;
}

.v-btn--variant-elevated {
    box-shadow: none;
}

.footer {
    background-color: rgb(35, 35, 46);
    color: white
}

.footer-topPage {
    background-color: rgb(73, 73, 82);
    text-align: center;
    color: white;
    display: flex;
    flex-direction: column;
}

.footer div {
    display: flex;
    justify-content: space-around;
}

.footer-sectionsList {
    display: flex;
    flex-wrap: wrap;
    background-color: rgb(53, 53, 58);
    padding-top: 0.7rem;
    padding-left: 0.7rem;
    padding-right: 0.7rem;
}

.footer-sectionsList li {
    width: 50%;
    color: white;
    white-space: nowrap;
    flex-grow: 0;
    margin-bottom: 0.7rem;
}

.footer-sectionsList li a {
    color: white;
}

.footer-account {
    padding-top: 2rem;
    font-size: 0.8rem;
    background-color: black;
    color: white;
    display: flex;
    flex-direction: column;
    text-align: center;
    flex-wrap: wrap;
}

.footer-settingsContainer {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    margin-bottom: 1rem;
}

.footer-account a {
    color: white;
    margin-bottom: 1rem;
}

.footer-settingsContainer span {
    white-space: nowrap;
}

.footer-useConditions,
.footer-rights {
    font-size: 0.7rem;
    color: rgb(151, 151, 151)
}

.footer-useConditions__span2 {
    margin-left: 1rem;
    margin-right: 1rem;
}

.footer-rights {
    margin-top: 0.5rem;
    margin-bottom: 2rem;
}

.leftNav-header {
    background-color: rgb(53, 53, 58);
    color: white;
}

#leftNav-account {
    padding-top: 1rem;
    display: flex;
    justify-content: end;
}

#leftNav-account p {
    font-size: 0.6rem;
    font-weight: 600;
}

#leftNav-account svg {
    width: 1rem;
}

.leftNav-title {
    display: flex;
    flex-direction: column;
    padding-left: 1rem;
}

.leftNav-title h3 {
    height: 1.2rem;
}

.leftNav-title h2 {
    height: 3rem;
}

.leftNav-home {
    display: flex;
    justify-content: space-between;
    color: black;
    padding-left: 1rem;
    padding-right: 1rem;
    font-weight: 600;
}

.leftNav-homeContainer {
    border-bottom: 0.3rem solid rgb(211, 192, 192);
}

.leftNav-trending {
    padding-left: 1rem;
    margin-top: 0.5rem;
    border-bottom: 0.3rem solid rgb(211, 192, 192);
}

.leftNav-trending p {
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
}

.leftNav-trending p a {
    color: rgb(35, 35, 46);
}

.leftNav-departments {
    padding-left: 1rem;
    margin-top: 0.5rem;
}

.leftNav-departments h3 {
    margin-bottom: 0.5rem;
}

.leftNav-departments ul li {
    margin-bottom: 0.5rem;
}

.leftNav-departments ul li a {
    color: rgb(35, 35, 46);
    text-decoration: none;
}

.rightNav-header {
    padding-left: 1rem;
    background-color: rgb(35, 35, 46);
    color: white;
}

#rightNav-browse {
    display: flex;
    justify-content: flex-end;
}

.rightNav-browse__text {
    font-size: 0.6rem;
}

.rightNav-browse__icon {
    width: 1rem;
}

.rightNav-title {
    display: flex;
    flex-direction: column;
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
}

.rightNav-header h3 {
    height: 1.3rem;
}
</style>