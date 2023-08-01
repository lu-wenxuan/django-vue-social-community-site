<template>
    <div class="max-w-7xl mx-auto grid grid-cols-3 gap-4">
        <div class="main-center col-span-2 space-y-4">
            <div class="bg-white border border-gray-200 text-center rounded-lg">
                <form v-on:submit.prevent="submitForm" method="post">
                <div class="p-4">
                    <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What are you thinking about?"></textarea>
                </div>

                <div class="p-4 border-t border-gray-100 flex justify-between">
                    <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Attach image</a>
                    <button href="#" class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Post</button>

                </div>
                </form>
            </div>


            <!---<div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="m-6 flex items-center justify-between">
                    <div class="flex items-center space-x-6">
                        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQh2ibh9YBLzRs29v8VE96dT1ow0TTfys_gAw&usqp=CAU" class="w-[40px] rounded-full">
                        <p><strong>Code with Wenxuan</strong></p>
                    </div>
                    <p class="text-gray-600">18 minutes age</p>
                </div>
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYQe403RAdmihMRMc88j66idCzC9pu17Rmww&usqp=CAU" class="rounded-lg w-full">
                
                
                <div class="my-6 flex justify-between">
                    <div class="flex space-x-6">
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
                                </svg>
                                <span class="text-gray-500 text-xs">82 likes</span>
                        </div>

                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M8.625 12a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 01-2.555-.337A5.972 5.972 0 015.41 20.97a5.969 5.969 0 01-.474-.065 4.48 4.48 0 00.978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25z" />
                            </svg>

                                <span class="text-gray-500 text-xs">0 comments</span>
                        </div>
                    </div>
                    <div>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                         <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z" />
                        </svg>
                    </div>
                </div>
            </div>-->


            <div class="p-4 bg-white border border-gray-200 rounded-lg"
                    v-for="post in posts"
                    v-bind:key="post.id"
            >
            <FeedItem v-bind:post="post"/>

            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow/>
            <Trends/>
        </div>
    </div>
</template>

<script>
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue';
import Trends from '../components/Trends.vue';
import axios from 'axios';
import FeedItem from '../components/FeedItem.vue'

export default {
    name: "FeedView",
    components: { PeopleYouMayKnow, Trends, FeedItem },

    data() {
        return {
            posts: [],
            body:''
        }
    },

    mounted() {
        this.getFeed()
    },

    methods:{
        getFeed(){
            axios
                .get('/api/posts')
                .then(response => {
                    console.log('data', response.data)
                    this.posts = response.data

                    console.log('data2',this.posts)
                })
                .catch(error => {
                    console.log('error',error)
                })
        },

        submitForm() {
            console.log('submitForm', this.body)

            axios
                .post('/api/posts/create/', {
                    'body': this.body
                })
                .then(response => {
                    console.log('data', response.data)

                    this.posts.unshift(response.data)
                    this.body=''
                })
                .catch(error => {
                    console.log('error',error)
                })
        }


    }


}
</script>