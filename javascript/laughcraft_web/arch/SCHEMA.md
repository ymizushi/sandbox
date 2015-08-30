### Postgres
- user
    * id 
    - username
    - email
    - password
    - thumbnail_image_url
    - create_time
    - update_time

- project
    * id
    * user_id
    - title
    - description
    - score
    - thumbnail_image_url
    - deleted
    - hidden
    - create_time
    - update_time

- preparation_projecs
    * id
    * user_id
    - title
    - description
    - score
    - create_time
    - update_time

- project_counter
    * project_id
    - comment_counter
    - view_counter

- mylist
    * user_id
    - project_ids

- project_tag
    * project_id
    - tags

- admin_user
    * id
    - email
    - password
    - create_time
    - update_time

### Redis
    - ranking_yymmdd_comment_count
    - ranking_yymmdd_view_count
