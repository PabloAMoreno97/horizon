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
                                <v-list>
                                    <v-list-item>
                                        <div>
                                            <p>Your Account</p>
                                            <v-btn color="transparent"
                                                @click.stop="(yourAccount = !yourAccount) && (browse = false)">
                                                <font-awesome-icon icon="fa-regular fa-user" class="header-userIcon" />
                                            </v-btn>
                                        </div>

                                        <h3>Browse</h3>
                                        <h3>Horizon</h3>
                                    </v-list-item>

                                </v-list>

                                <v-divider></v-divider>

                                <v-list density="compact" nav>
                                    <v-list-item prepend-icon="mdi-view-dashboard" title="Home" value="home">
                                    </v-list-item>
                                    <v-list-item prepend-icon="mdi-forum" title="About" value="about"></v-list-item>
                                </v-list>
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
                                    <v-list-item prepend-avatar="https://randomuser.me/api/portraits/men/78.jpg"
                                        title="John Leider">
                                    </v-list-item>

                                    <v-divider></v-divider>

                                    <v-list density="compact" nav>
                                        <v-list-item prepend-icon="mdi-view-dashboard" title="Home" value="home">
                                        </v-list-item>
                                        <v-list-item prepend-icon="mdi-forum" title="About" value="about"></v-list-item>
                                    </v-list>
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
                    <li><a href="#">Your Recalls and Product Safety Alerts</a></li>
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
</style>