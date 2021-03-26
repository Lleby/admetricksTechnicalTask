from instagramProfile.services import InstagramScraperService

class InstagramScraperLogic:

    @staticmethod
    def add_user_profile(user_login, password_login, user_names):
        
        scraper = InstagramScraperService.login(user_login, password_login)
        tables_state = InstagramScraperService.create_tables()

        post_info = []
        user_info = []
        for user in user_names:

            if not InstagramScraperService.check_if_exist(user):
                profile, posts = InstagramScraperService.get_instagram_profiles(user, scraper)
                user_info.append((profile.userid, user, profile.full_name, profile.followers, profile.followees))

                if profile.is_private:
                    print("This profile is private (probably no posts were stored):", user)

                for post in posts:

                    if (post.is_video):
                        media = InstagramScraperService.get_media_from_url(post.video_url)

                    else:
                        media = InstagramScraperService.get_media_from_url(post.url)

                    post_info.append((post.mediaid, profile.userid, post.date, post.caption, media, post.likes, post.comments, post.video_view_count))
            
            else:
                print("This user is already in DB:", user)

        result = InstagramScraperService.insert_user_db(user_info, post_info)

        return result