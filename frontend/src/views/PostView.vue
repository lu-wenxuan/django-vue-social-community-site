<template>
    <div class="max-w-7xl mx-auto grid grid-cols-3 gap-4">
        <div class="main-center col-span-2 space-y-4">
            <!---<div class="bg-white border border-gray-200 text-center rounded-lg">
                <form v-on:submit.prevent="submitForm" method="post">
                <div class="p-4">
                    <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What are you thinking about?"></textarea>
                </div>

                <div class="p-4 border-t border-gray-100 flex justify-between">
                    <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Attach image</a>
                    <button href="#" class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Post</button>

                </div>
                </form>
            </div>-->


            <div class="p-4 bg-white border border-gray-200 rounded-lg"                  
                    v-if="post.id"
            >
            <FeedItem v-bind:post="post"/>
            </div>

            <div
                class="p-4 ml-6 bg-white border border-gray-200 rounded-lg"
                v-for="comment in post.comments"
                v-bind:key="comment.id"
            >
                <CommentItem v-bind:comment="comment"/>

            </div>

             <div class="bg-white border border-gray-200 text-center rounded-lg">
                <form v-on:submit.prevent="submitForm" method="post">
                <div class="p-4">
                    <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What do you think?"></textarea>
                </div>

                <div class="p-4 border-t border-gray-100 flex justify-between">
                
                    <button href="#" class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Comment</button>

                </div>
                </form>
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
import FeedItem from '../components/FeedItem.vue';
import CommentItem from '../components/CommentItem.vue';


export default {
    name: "PostView",
    components: { PeopleYouMayKnow, Trends, FeedItem, CommentItem },

    data() {
        return {
            post: {
                id: null,
                comments:[]
            },
            body: ''
            
        }
    },

    mounted() {
        this.getPost()
    },

    methods:{
        getPost(){
            axios
                .get(`/api/posts/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)
                    this.post = response.data.post

        
                })
                .catch(error => {
                    console.log('error',error)
                })
        },

        submitForm() {
            console.log('submitForm', this.body)

            axios
                .post(`/api/posts/${this.$route.params.id}/comment/`, {
                    'body': this.body
                })
                .then(response => {
                    console.log('data', response.data)

                    this.post.comments.push(response.data)
                    this.post.comments_count += 1
                    this.body=''
                })
                .catch(error => {
                    console.log('error',error)
                })
        }

       

    }


}
</script>