USER

| Field       | Type     |
| ----------- | -------- |
| id          | Auto     |
| username    | String   |
| email       | String   |
| password    | Hashed   |
| first_name  | String   |
| last_name   | String   |
| date_joined | DateTime |

PROBLEM

| Field         | Type     |
| ------------- | -------- |
| id            | Auto     |
| title         | String   |
| slug          | String   |
| statement     | Text     |
| input_format  | Text     |
| output_format | Text     |
| constraints   | Text     |
| sample_input  | Text     |
| sample_output | Text     |
| explanation   | Text     |
| difficulty    | Choice   |
| created_at    | DateTime |

SUBMISSION

| Field          | Type        |
| -------------- | ----------- |
| id             | Auto        |
| user           | FK(User)    |
| problem        | FK(Problem) |
| language       | Choice      |
| code           | Text        |
| verdict        | Choice      |
| execution_time | Float       |
| memory_used    | Float       |
| submitted_at   | DateTime    |

CONTEXT

| Field       | Type     |
| ----------- | -------- |
| id          | Auto     |
| title       | String   |
| description | Text     |
| start_time  | DateTime |
| end_time    | DateTime |

CONTEXTPARTICIPANT

| Field   | Type    |
| ------- | ------- |
| id      | Auto    |
| contest | FK      |
| user    | FK      |
| score   | Integer |
| rank    | Integer |

TAG

| Field | Type   |
| ----- | ------ |
| id    | Auto   |
| name  | String |
