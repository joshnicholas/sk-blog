<script>
    import { name } from '$lib/info.js'

    import PostsList from '$lib/components/ScribblesList.svelte'
    
    import { browser } from '$app/environment'
    import { format } from 'date-fns'
    import { parse } from 'node-html-parser'
    import parseMD from 'parse-md'
    import fs from 'fs'
    import path from 'path'
    import { marked } from 'marked';

    import process from 'process';

    let stem = 'scribbles'
  
    // console.log(posts)
    // console.log(name)
  
    // $: isFirstPage = data.page === 1
    // $: hasNextPage = data.posts[data.posts.length - 1]?.previous

    // console.log("Current directory:", process.cwd());


    
    const posts = Object.entries(import.meta.glob("./scribbles/*.md", { eager: false }))
     

    
    .map(([filepath, post]) => {

    //     let pathos = path.join(process.cwd(), filepath)
    //     // console.log("pathos: ", pathos)
    //     const fileContents = fs.readFileSync(pathos, 'utf8')
    //     const { metadata, content } = parseMD(fileContents)
    //     console.log(content)
    //     console.log(metadata)
    })


        // console.log(filepath)
        // console.log(post.default.render().html)



        // let pathos = path.resolve(, filepath)

        // console.log(pathos)

        // const fileContents = fs.readFileSync(filepath, 'utf8')
        // const { metadata, content } = parseMD(fileContents)

        // console.log(post.default.render())
        // const html = parse(post.default.render().html)
        // console.log(html)
    // })

  $: console.log(posts)

  </script>


<!-- <PostsList posts={data.posts} /> -->