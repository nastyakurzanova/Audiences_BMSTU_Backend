package models

type AudiencesFreeRequest struct {
	AccessToken int64 `json:"access_token"`
	// !!!!!!!!!!!!!!!!!
	AudiencesFree int `json:"free_audiences"`
}
